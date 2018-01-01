grammar SimpleC;

start : (include)* function ;

include : '#include' '<' ID '.' ID '>' ;

function : type ID '(' ')' '{' (stat | block)* '}' ;

type : 'int' | 'char' ;

// block是需要加{}的if else while语句块
block : ifBlock
	  | elifBlock
	  | elseBlock
	  | whileBlock
	  ;

ifBlock : 'if' '(' expr (CONNECTOR expr)* ')' '{' (stat | block)* '}' ;

elifBlock : 'else if' '(' expr (CONNECTOR expr)* ')' '{' (stat | block)* '}' ;

elseBlock : 'else' '{' (stat | block)* '}' ;

whileBlock : 'while' '(' expr (CONNECTOR expr)* ')' '{' (stat | block)* '}' ;


stat :  declareStat
	 |  assignStat
	 |  returnStat
	 |  printfStat
	 ;

// 可以出现在等式右边或判断条件中的表达式,包括三个标准库函数
expr : ID('[' (INT|ID) ']')? OPERATOR ID('[' (INT|ID) ']')?
	 | ID('[' (INT|ID) ']')? OPERATOR INT
	 | ID('[' (INT|ID) ']')? OPERATOR CHAR
	 | INT OPERATOR INT
	 | exprFunc
	 ;


exprFunc : strlenFunc
		 | atoiFunc
		 | isdigitFunc
		 ;

// 在程序中用到的三个函数
strlenFunc : 'strlen' '(' ID ')' ;

atoiFunc : 'atoi' '(' ID ')' ;

isdigitFunc : 'isdigit' '(' ID ')' ;

// 声明语句
// 第四条：如int a[100]
// 第五条: 如char a[100] = "hello"
declareStat : type ID ';'
			| type ID '=' ID ';'
			| type ID '=' INT ';'
			| type ID '[' (INT)? ']' ';'
			| type ID '[' (INT)? ']' '=' STRING ';'
			;

// 赋值语句
// 后四条包括了数组中元素的赋值
assignStat : ID '=' ID ';'
		   | ID ('[' (INT|ID) ']')? '=' ID ('[' (INT|ID) ']')? ';'
		   | ID ('[' (INT|ID) ']')? '=' INT ';'
		   | ID ('[' (INT|ID) ']')? '=' CHAR ';'
		   | ID ('[' (INT|ID) ']')? '=' expr ';'
		   ;

// 返回语句
returnStat : 'return' INT ';' ;

// 打印语句
// 参数为字符串或多个变量
printfStat : 'printf' '(' STRING ')' ';'
           | 'printf' '(' ID (',' ID)* ')' ';'
           ;

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