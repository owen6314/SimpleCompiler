grammar SimpleC;

start : (include)* (function)* ;

include : '#include' '<' mID '.' mID '>' ;

function : mType mID '(' formalParams ')' '{' content '}' ;

formalParams : formalParam | formalParam ',' formalParams |;

formalParam : mType mID ;

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
     |  customFuncStat
     ;

expr : (mID | mInt | mChar | mString | designator | exprFunc ) mOperator expr
     | (mID | mInt | mChar | mString | designator | exprFunc )
     ;

designator : mID '[' (mInt|mID) ']';

arrayNoInit : mID '[' ']' ;

exprFunc : strlenFunc
     | atoiFunc
     | isdigitFunc
         | customFunc
     ;

// 在程序中用到的三个函数
strlenFunc : 'strlen' '(' mID ')' ;

atoiFunc : 'atoi' '(' mID ')' ;

isdigitFunc : 'isdigit' '(' mID ')' ;

customFunc : mID '(' actualParams ')' ;

actualParams : actualParam | actualParam ',' actualParams |;

actualParam : mID | mInt ;

declareStat : arrayDeclareStat
            | otherDeclareStat
            ;

arrayDeclareStat : mType mID '[' expr ']' ';' ;

otherDeclareStat :  mType (mID|designator|arrayNoInit) '=' expr ';'
                 |  mType mID ';'
                 ;


assignStat : (mID | designator) '=' expr ';' ;

// 返回语句
returnStat : 'return' expr ';' ;

// 打印语句
// 参数为字符串或多个变量
printfStat : 'printf' '(' mString ')' ';'
           | 'printf' '(' mID (',' mID)* ')' ';'
           ;

customFuncStat :  customFunc ';' ;

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
    :   [ \t\r\n]+
        -> skip
    ;
