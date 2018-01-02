grammar SimpleC;

start : (include)* function ;

include : '#include' '<' mID '.' mID '>' ;

function : mType mID '(' ')' '{' content '}' ;

mType : 'int' | 'char' ;

content : (stat|block) content
        | (stat|block)
        |
        ;

// block是需要加{}的if else while语句块
block : ifBlock
	  | elifBlock
	  | elseBlock
	  | whileBlock
	  ;


ifBlock : 'if' '(' condition ')' '{' content '}' ;

elifBlock : 'else if' '(' condition ')' '{' content '}' ;

elseBlock : 'else' '{' content '}' ;

whileBlock : 'while' '(' condition ')' '{' content '}' ;

condition : expr mConnector condition
          | expr
          ;

stat :  declareStat
	 |  assignStat
	 |  returnStat
	 |  printfStat
	 ;

// 可以出现在等式右边或判断条件中的表达式,包括三个标准库函数
/*expr : mID('[' (mInt|mID) ']')? mOperator mID('[' (mInt|mID) ']')?
	 | mID('[' (mInt|mID) ']')? mOperator mInt
	 | mID('[' (mInt|mID) ']')? mOperator mChar
	 | mInt mOperator mInt
	 | exprFunc
	 ;*/

expr : (mID | mInt | mChar | mString | designator | exprFunc ) mOperator expr
     | (mID | mInt | mChar | mString | designator | exprFunc )
	 ;

designator : mID '[' (mInt|mID) ']';

arrayNoInit : mID '[' ']' ;

exprFunc : strlenFunc
		 | atoiFunc
		 | isdigitFunc
		 ;

// 在程序中用到的三个函数
strlenFunc : 'strlen' '(' mID ')' ;

atoiFunc : 'atoi' '(' mID ')' ;

isdigitFunc : 'isdigit' '(' mID ')' ;

// 声明语句
// 第四条：如int a[100]
// 第五条: 如char a[100] = "hello"
//declareStat : mType mID ';'
//			| mType mID '=' mID ';'
//			| mType mID '=' mInt ';'
//			| mType mID '[' (mInt)? ']' ';'
//			| mType mID '[' (mInt)? ']' '=' mString ';'
//			;

declareStat : mType (mID|designator) ';'
            | mType (mID|designator|arrayNoInit) '=' expr ';'
            ;

// 赋值语句
// 后四条包括了数组中元素的赋值
/*assignStat : mID '=' mID ';'
		   | mID ('[' (mInt|mID) ']')? '=' mID ('[' (mInt|mID) ']')? ';'
		   | mID ('[' (mInt|mID) ']')? '=' mInt ';'
		   | mID ('[' (mInt|mID) ']')? '=' mChar ';'
		   | mID ('[' (mInt|mID) ']')? '=' expr ';'
		   ;*/

assignStat : (mID | designator) '=' expr ';' ;

// 返回语句
returnStat : 'return' mInt ';' ;

// 打印语句
// 参数为字符串或多个变量
printfStat : 'printf' '(' mString ')' ';'
           | 'printf' '(' mID (',' mID)* ')' ';'
           ;
           
mOperator : OPERATOR;

mConnector : CONNECTOR;

mInt : INT;

mChar : CHAR;

mString : STRING;

mID : ID;

// lexical rules

OPERATOR : '+' | '-' | '*' | '/' | '==' | '!=' | '<=' | '>=' | '>' | '<' ;

CONNECTOR : '&&' | '||' ;

INT : ('-')?[0-9]+ ;

CHAR : '\'' . '\'' ;

STRING : '"' .*? '"' ;

ID : [a-zA-Z][a-zA-Z0-9_]* ;  //identifier必须由字母开头，含有数字、字母或下划线

//comments and white spaces
BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;
WS
	: 	[ \t\r\n]+ 
	 	-> skip 
	;
