import sys
from antlr4 import *
from SimpleCLexer import SimpleCLexer
from SimpleCParser import SimpleCParser
from translate_visitor import TranslateVisitor


def main(argv):
    input = FileStream(argv[1])
    lexer = SimpleCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleCParser(stream)
    tree = parser.start()
    output_file = open(argv[2], "w+")
    eval = TranslateVisitor(output_file)
    eval.visit(tree)
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)