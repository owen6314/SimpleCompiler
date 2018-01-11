# Generated from /Users/aglax2357/Projects/antlr_parse/src/SimpleC.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCParser.

class SimpleCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleCParser#start.
    def visitStart(self, ctx:SimpleCParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#include.
    def visitInclude(self, ctx:SimpleCParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function.
    def visitFunction(self, ctx:SimpleCParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#formalParams.
    def visitFormalParams(self, ctx:SimpleCParser.FormalParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#formalParam.
    def visitFormalParam(self, ctx:SimpleCParser.FormalParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mType.
    def visitMType(self, ctx:SimpleCParser.MTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#content.
    def visitContent(self, ctx:SimpleCParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#block.
    def visitBlock(self, ctx:SimpleCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#ifBlock.
    def visitIfBlock(self, ctx:SimpleCParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#elifBlock.
    def visitElifBlock(self, ctx:SimpleCParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#elseBlock.
    def visitElseBlock(self, ctx:SimpleCParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#whileBlock.
    def visitWhileBlock(self, ctx:SimpleCParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#condition.
    def visitCondition(self, ctx:SimpleCParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#stat.
    def visitStat(self, ctx:SimpleCParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#expr.
    def visitExpr(self, ctx:SimpleCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#designator.
    def visitDesignator(self, ctx:SimpleCParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arrayNoInit.
    def visitArrayNoInit(self, ctx:SimpleCParser.ArrayNoInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#exprFunc.
    def visitExprFunc(self, ctx:SimpleCParser.ExprFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#strlenFunc.
    def visitStrlenFunc(self, ctx:SimpleCParser.StrlenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#atoiFunc.
    def visitAtoiFunc(self, ctx:SimpleCParser.AtoiFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#isdigitFunc.
    def visitIsdigitFunc(self, ctx:SimpleCParser.IsdigitFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#customFunc.
    def visitCustomFunc(self, ctx:SimpleCParser.CustomFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#actualParams.
    def visitActualParams(self, ctx:SimpleCParser.ActualParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#actualParam.
    def visitActualParam(self, ctx:SimpleCParser.ActualParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#declareStat.
    def visitDeclareStat(self, ctx:SimpleCParser.DeclareStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arrayDeclareStat.
    def visitArrayDeclareStat(self, ctx:SimpleCParser.ArrayDeclareStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#otherDeclareStat.
    def visitOtherDeclareStat(self, ctx:SimpleCParser.OtherDeclareStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#assignStat.
    def visitAssignStat(self, ctx:SimpleCParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#returnStat.
    def visitReturnStat(self, ctx:SimpleCParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#printfStat.
    def visitPrintfStat(self, ctx:SimpleCParser.PrintfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#customFuncStat.
    def visitCustomFuncStat(self, ctx:SimpleCParser.CustomFuncStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mOperator.
    def visitMOperator(self, ctx:SimpleCParser.MOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mConnector.
    def visitMConnector(self, ctx:SimpleCParser.MConnectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mInt.
    def visitMInt(self, ctx:SimpleCParser.MIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mChar.
    def visitMChar(self, ctx:SimpleCParser.MCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mString.
    def visitMString(self, ctx:SimpleCParser.MStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#mID.
    def visitMID(self, ctx:SimpleCParser.MIDContext):
        return self.visitChildren(ctx)



del SimpleCParser