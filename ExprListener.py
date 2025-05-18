# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#datosPacienteSentence.
    def enterDatosPacienteSentence(self, ctx:ExprParser.DatosPacienteSentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#datosPacienteSentence.
    def exitDatosPacienteSentence(self, ctx:ExprParser.DatosPacienteSentenceContext):
        pass


    # Enter a parse tree produced by ExprParser#diagnosticoSentence.
    def enterDiagnosticoSentence(self, ctx:ExprParser.DiagnosticoSentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#diagnosticoSentence.
    def exitDiagnosticoSentence(self, ctx:ExprParser.DiagnosticoSentenceContext):
        pass


    # Enter a parse tree produced by ExprParser#fechasSentence.
    def enterFechasSentence(self, ctx:ExprParser.FechasSentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#fechasSentence.
    def exitFechasSentence(self, ctx:ExprParser.FechasSentenceContext):
        pass


    # Enter a parse tree produced by ExprParser#medicamentoSentence.
    def enterMedicamentoSentence(self, ctx:ExprParser.MedicamentoSentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#medicamentoSentence.
    def exitMedicamentoSentence(self, ctx:ExprParser.MedicamentoSentenceContext):
        pass



del ExprParser