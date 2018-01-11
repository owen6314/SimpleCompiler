# Generated from /Users/aglax2357/Projects/antlr_parse/src/SimpleC.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCParser.

from SimpleCVisitor import SimpleCVisitor


class TranslateVisitor(SimpleCVisitor):
    indentation = 0
    
    def print_indentation(self):
        for i in range(self.indentation):
            print("    ", end="")
    
    def emit(self, *args):
        for arg in args:
            print(arg, end="")
            
    def entry(self):
        self.emit("\nif __name__ == '__main__':\n")
        self.emit("    main()")
    
    def check_type(self):
        pass
    
    # [DONE] Visit a parse tree produced by SimpleCParser#start.
    def visitStart(self, ctx: SimpleCParser.StartContext):
        self.visitChildren(ctx)
        self.entry()
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#include.
    def visitInclude(self, ctx: SimpleCParser.IncludeContext):
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#function.
    def visitFunction(self, ctx: SimpleCParser.FunctionContext):
        self.emit("def ")
        self.visit(ctx.getChild(1))
        self.emit("(")
        self.visit(ctx.getChild(3))
        self.emit("):\n")
        self.indentation += 1
        self.visit(ctx.getChild(6))
        self.indentation -= 1
        return
    
    # Visit a parse tree produced by SimpleCParser#params.
    def visitParams(self, ctx: SimpleCParser.ParamsContext):
        if ctx.getChildCount() == 3:
            self.visit(ctx.getChild(0))
            self.emit(", ")
            self.visit(ctx.getChild(2))
        elif ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
        return
    
    # Visit a parse tree produced by SimpleCParser#param.
    def visitParam(self, ctx: SimpleCParser.ParamContext):
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mType.
    def visitMType(self, ctx: SimpleCParser.MTypeContext):
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#content.
    def visitContent(self, ctx: SimpleCParser.ContentContext):
        self.visitChildren(ctx)
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#block.
    def visitBlock(self, ctx: SimpleCParser.BlockContext):
        self.print_indentation()
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#ifBlock.
    def visitIfBlock(self, ctx: SimpleCParser.IfBlockContext):
        self.emit("if ")
        self.visitChildren(ctx.getChild(2))
        self.emit(":\n")
        self.visitChildren(ctx.getChild(5))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#elifBlock.
    def visitElifBlock(self, ctx: SimpleCParser.ElifBlockContext):
        self.emit("elif ")
        self.visitChildren(ctx.getChild(2))
        self.emit(":\n")
        self.visitChildren(ctx.getChild(5))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#elseBlock.
    def visitElseBlock(self, ctx: SimpleCParser.ElseBlockContext):
        self.emit("else:\n")
        self.visitChildren(ctx.getChild(2))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#whileBlock.
    def visitWhileBlock(self, ctx: SimpleCParser.WhileBlockContext):
        self.emit("while ")
        self.visitChildren(ctx.getChild(2))
        self.emit(":\n")
        self.visitChildren(ctx.getChild(5))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#condition.
    def visitCondition(self, ctx: SimpleCParser.ConditionContext):
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#stat.
    def visitStat(self, ctx: SimpleCParser.StatContext):
        self.print_indentation()
        self.visitChildren(ctx)
        self.emit("\n")
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#expr.
    def visitExpr(self, ctx: SimpleCParser.ExprContext):
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#designator.
    def visitDesignator(self, ctx: SimpleCParser.DesignatorContext):
        self.visit(ctx.getChild(0))
        self.emit("[")
        self.visit(ctx.getChild(2))
        self.emit("]")
        return
    
    # Visit a parse tree produced by SimpleCParser#arrayNoInit.
    def visitArrayNoInit(self, ctx: SimpleCParser.ArrayNoInitContext):
        # self.visit(ctx.getChild(0))
        # self.emit("[]")
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SimpleCParser#exprFunc.
    def visitExprFunc(self, ctx: SimpleCParser.ExprFuncContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SimpleCParser#strlenFunc.
    def visitStrlenFunc(self, ctx: SimpleCParser.StrlenFuncContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SimpleCParser#atoiFunc.
    def visitAtoiFunc(self, ctx: SimpleCParser.AtoiFuncContext):
        self.emit('int("".join(')
        self.visit(ctx.getChild(2))
        self.emit('[:')
        self.visit(ctx.getChild(2))
        self.emit('.index(0)]))')
        return
    
    # Visit a parse tree produced by SimpleCParser#isdigitFunc.
    def visitIsdigitFunc(self, ctx: SimpleCParser.IsdigitFuncContext):
        self.visit(ctx.getChild(2))
        self.emit(".isdigit()")
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#declareStat.
    def visitDeclareStat(self, ctx: SimpleCParser.DeclareStatContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SimpleCParser#arrayDeclareStat.
    def visitArrayDeclareStat(self, ctx: SimpleCParser.ArrayDeclareStatContext):
        self.visit(ctx.getChild(1))
        self.emit(' = [None] * ')
        self.visit(ctx.getChild(3))
        return
    
    # Visit a parse tree produced by SimpleCParser#otherDeclareStat.
    def visitOtherDeclareStat(self, ctx: SimpleCParser.OtherDeclareStatContext):
        if (ctx.getChildCount() == 5):
            self.visit(ctx.getChild(1))
            self.emit(" = ")
            self.visit(ctx.getChild(3))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#assignStat.
    def visitAssignStat(self, ctx: SimpleCParser.AssignStatContext):
        self.visit(ctx.getChild(0))
        self.emit(" = ")
        self.visit(ctx.getChild(2))
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#returnStat.
    def visitReturnStat(self, ctx: SimpleCParser.ReturnStatContext):
        self.emit("return ")
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#printfStat.
    def visitPrintfStat(self, ctx: SimpleCParser.PrintfStatContext):
        if ctx.getChildCount() == 5:
            self.emit("print(")
            self.visit(ctx.getChild(2))
            self.emit(")")
        else:
            self.emit("print(")
            self.visit(ctx.getChild(2))
            self.emit(" % (")
            for i in range(4, ctx.getChildCount() - 2, 2):
                self.visit(ctx.getChild(i))
                self.emit(',')
            self.emit("))")
        return
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mOperator.
    def visitMOperator(self, ctx: SimpleCParser.MOperatorContext):
        self.emit(" ", ctx.OPERATOR().getText(), " ")
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mConnector.
    def visitMConnector(self, ctx: SimpleCParser.MConnectorContext):
        if ctx.CONNECTOR().getText() == "||":
            self.emit(" or ")
        elif ctx.CONNECTOR().getText() == "&&":
            self.emit(" and ")
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mInt.
    def visitMInt(self, ctx: SimpleCParser.MIntContext):
        self.emit(ctx.INT().getText())
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mChar.
    def visitMChar(self, ctx: SimpleCParser.MCharContext):
        self.emit(ctx.CHAR().getText())
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mString.
    def visitMString(self, ctx: SimpleCParser.MStringContext):
        self.emit(ctx.STRING().getText())
        return self.visitChildren(ctx)
    
    # [DONE] Visit a parse tree produced by SimpleCParser#mID.
    def visitMID(self, ctx: SimpleCParser.MIDContext):
        self.emit(ctx.ID().getText())
        return self.visitChildren(ctx)


del SimpleCParser
