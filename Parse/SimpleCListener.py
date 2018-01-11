# Generated from /Users/aglax2357/Projects/antlr_parse/src/SimpleC.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete listener for a parse tree produced by SimpleCParser.
class SimpleCListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCParser#start.
    def enterStart(self, ctx:SimpleCParser.StartContext):
        pass

    # Exit a parse tree produced by SimpleCParser#start.
    def exitStart(self, ctx:SimpleCParser.StartContext):
        pass


    # Enter a parse tree produced by SimpleCParser#include.
    def enterInclude(self, ctx:SimpleCParser.IncludeContext):
        pass

    # Exit a parse tree produced by SimpleCParser#include.
    def exitInclude(self, ctx:SimpleCParser.IncludeContext):
        pass


    # Enter a parse tree produced by SimpleCParser#function.
    def enterFunction(self, ctx:SimpleCParser.FunctionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#function.
    def exitFunction(self, ctx:SimpleCParser.FunctionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#params.
    def enterParams(self, ctx:SimpleCParser.ParamsContext):
        pass

    # Exit a parse tree produced by SimpleCParser#params.
    def exitParams(self, ctx:SimpleCParser.ParamsContext):
        pass


    # Enter a parse tree produced by SimpleCParser#param.
    def enterParam(self, ctx:SimpleCParser.ParamContext):
        pass

    # Exit a parse tree produced by SimpleCParser#param.
    def exitParam(self, ctx:SimpleCParser.ParamContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mType.
    def enterMType(self, ctx:SimpleCParser.MTypeContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mType.
    def exitMType(self, ctx:SimpleCParser.MTypeContext):
        pass


    # Enter a parse tree produced by SimpleCParser#content.
    def enterContent(self, ctx:SimpleCParser.ContentContext):
        pass

    # Exit a parse tree produced by SimpleCParser#content.
    def exitContent(self, ctx:SimpleCParser.ContentContext):
        pass


    # Enter a parse tree produced by SimpleCParser#block.
    def enterBlock(self, ctx:SimpleCParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#block.
    def exitBlock(self, ctx:SimpleCParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#ifBlock.
    def enterIfBlock(self, ctx:SimpleCParser.IfBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#ifBlock.
    def exitIfBlock(self, ctx:SimpleCParser.IfBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#elifBlock.
    def enterElifBlock(self, ctx:SimpleCParser.ElifBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#elifBlock.
    def exitElifBlock(self, ctx:SimpleCParser.ElifBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#elseBlock.
    def enterElseBlock(self, ctx:SimpleCParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#elseBlock.
    def exitElseBlock(self, ctx:SimpleCParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#whileBlock.
    def enterWhileBlock(self, ctx:SimpleCParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#whileBlock.
    def exitWhileBlock(self, ctx:SimpleCParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#condition.
    def enterCondition(self, ctx:SimpleCParser.ConditionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#condition.
    def exitCondition(self, ctx:SimpleCParser.ConditionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#stat.
    def enterStat(self, ctx:SimpleCParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#stat.
    def exitStat(self, ctx:SimpleCParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expr.
    def enterExpr(self, ctx:SimpleCParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expr.
    def exitExpr(self, ctx:SimpleCParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleCParser#designator.
    def enterDesignator(self, ctx:SimpleCParser.DesignatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#designator.
    def exitDesignator(self, ctx:SimpleCParser.DesignatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#arrayNoInit.
    def enterArrayNoInit(self, ctx:SimpleCParser.ArrayNoInitContext):
        pass

    # Exit a parse tree produced by SimpleCParser#arrayNoInit.
    def exitArrayNoInit(self, ctx:SimpleCParser.ArrayNoInitContext):
        pass


    # Enter a parse tree produced by SimpleCParser#exprFunc.
    def enterExprFunc(self, ctx:SimpleCParser.ExprFuncContext):
        pass

    # Exit a parse tree produced by SimpleCParser#exprFunc.
    def exitExprFunc(self, ctx:SimpleCParser.ExprFuncContext):
        pass


    # Enter a parse tree produced by SimpleCParser#strlenFunc.
    def enterStrlenFunc(self, ctx:SimpleCParser.StrlenFuncContext):
        pass

    # Exit a parse tree produced by SimpleCParser#strlenFunc.
    def exitStrlenFunc(self, ctx:SimpleCParser.StrlenFuncContext):
        pass


    # Enter a parse tree produced by SimpleCParser#atoiFunc.
    def enterAtoiFunc(self, ctx:SimpleCParser.AtoiFuncContext):
        pass

    # Exit a parse tree produced by SimpleCParser#atoiFunc.
    def exitAtoiFunc(self, ctx:SimpleCParser.AtoiFuncContext):
        pass


    # Enter a parse tree produced by SimpleCParser#isdigitFunc.
    def enterIsdigitFunc(self, ctx:SimpleCParser.IsdigitFuncContext):
        pass

    # Exit a parse tree produced by SimpleCParser#isdigitFunc.
    def exitIsdigitFunc(self, ctx:SimpleCParser.IsdigitFuncContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declareStat.
    def enterDeclareStat(self, ctx:SimpleCParser.DeclareStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declareStat.
    def exitDeclareStat(self, ctx:SimpleCParser.DeclareStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#arrayDeclareStat.
    def enterArrayDeclareStat(self, ctx:SimpleCParser.ArrayDeclareStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#arrayDeclareStat.
    def exitArrayDeclareStat(self, ctx:SimpleCParser.ArrayDeclareStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#otherDeclareStat.
    def enterOtherDeclareStat(self, ctx:SimpleCParser.OtherDeclareStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#otherDeclareStat.
    def exitOtherDeclareStat(self, ctx:SimpleCParser.OtherDeclareStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#assignStat.
    def enterAssignStat(self, ctx:SimpleCParser.AssignStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#assignStat.
    def exitAssignStat(self, ctx:SimpleCParser.AssignStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#returnStat.
    def enterReturnStat(self, ctx:SimpleCParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#returnStat.
    def exitReturnStat(self, ctx:SimpleCParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#printfStat.
    def enterPrintfStat(self, ctx:SimpleCParser.PrintfStatContext):
        pass

    # Exit a parse tree produced by SimpleCParser#printfStat.
    def exitPrintfStat(self, ctx:SimpleCParser.PrintfStatContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mOperator.
    def enterMOperator(self, ctx:SimpleCParser.MOperatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mOperator.
    def exitMOperator(self, ctx:SimpleCParser.MOperatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mConnector.
    def enterMConnector(self, ctx:SimpleCParser.MConnectorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mConnector.
    def exitMConnector(self, ctx:SimpleCParser.MConnectorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mInt.
    def enterMInt(self, ctx:SimpleCParser.MIntContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mInt.
    def exitMInt(self, ctx:SimpleCParser.MIntContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mChar.
    def enterMChar(self, ctx:SimpleCParser.MCharContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mChar.
    def exitMChar(self, ctx:SimpleCParser.MCharContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mString.
    def enterMString(self, ctx:SimpleCParser.MStringContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mString.
    def exitMString(self, ctx:SimpleCParser.MStringContext):
        pass


    # Enter a parse tree produced by SimpleCParser#mID.
    def enterMID(self, ctx:SimpleCParser.MIDContext):
        pass

    # Exit a parse tree produced by SimpleCParser#mID.
    def exitMID(self, ctx:SimpleCParser.MIDContext):
        pass


