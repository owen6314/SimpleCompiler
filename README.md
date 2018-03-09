# SimpleCompiler
A really naive C-to-python compiler, project for course **编译原理** in THU

## 简介
实现C语言转Python，解析函数字符串表达式求值。即在程序中定义一个字符串表达式变量，在控制台上输出它的值。
## 语法解析
词法和语法的解析使用了ANTLR4。

目前编译器可以支持的语法有

- include语句(目前翻译的方法是忽略)
- 声明语句
- 赋值语句
- 表达式语句
- if,else条件判断
- while循环
- 函数
- atoi、strlen等C中的自带函数
- printf函数，用于打印结果
- 注释

## 翻译

翻译是在语法分析树的帮助下完成的，并通过非终结符的综合属性，实现了翻译和简单的语法检查的功能。具体来说，我们使用Visitor工具对整个语法分析树进行后根遍历，自下向上的对源代码进行翻译。翻译器支持的语法如下：

- 声明语句：支持多种类型（int char）、支持数组、支持为变量设初始值、重定义变量时报错
- 赋值语句：支持对数组中的元素进行赋值
- 表达式：支持在表达式中插入函数
- if,else条件判断：支持嵌套
- while循环：支持嵌套
- 函数
- atoi、strlen等库函数
- printf函数，用于打印结果

## 使用方法

1. 使用Python3，并安装antlr4-python3-runtime模块
2. 将`input.c`翻译为`output.py`

	```
	python parse.py <input.c> <output.py>
	```
