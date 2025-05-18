# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,1,1,1,5,1,27,8,1,
        10,1,12,1,30,9,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,
        1,2,1,2,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,5,3,67,8,3,10,
        3,12,3,70,9,3,1,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,1,3,1,4,1,
        4,5,4,83,8,4,10,4,12,4,86,9,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,
        9,4,1,4,1,4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,1,4,1,4,5,4,107,
        8,4,10,4,12,4,110,9,4,1,4,1,4,1,4,5,4,115,8,4,10,4,12,4,118,9,4,
        1,4,4,4,121,8,4,11,4,12,4,122,1,4,1,4,5,4,127,8,4,10,4,12,4,130,
        9,4,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,145,0,22,1,0,0,0,2,24,1,
        0,0,0,4,48,1,0,0,0,6,57,1,0,0,0,8,80,1,0,0,0,10,11,3,2,1,0,11,12,
        5,0,0,1,12,23,1,0,0,0,13,14,3,4,2,0,14,15,5,0,0,1,15,23,1,0,0,0,
        16,17,3,8,4,0,17,18,5,0,0,1,18,23,1,0,0,0,19,20,3,6,3,0,20,21,5,
        0,0,1,21,23,1,0,0,0,22,10,1,0,0,0,22,13,1,0,0,0,22,16,1,0,0,0,22,
        19,1,0,0,0,23,1,1,0,0,0,24,28,5,1,0,0,25,27,5,12,0,0,26,25,1,0,0,
        0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,
        1,0,0,0,31,32,5,8,0,0,32,36,5,2,0,0,33,35,5,12,0,0,34,33,1,0,0,0,
        35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,
        0,0,0,39,40,5,9,0,0,40,41,5,9,0,0,41,42,5,9,0,0,42,43,5,9,0,0,43,
        44,5,9,0,0,44,45,5,9,0,0,45,46,5,9,0,0,46,47,5,9,0,0,47,3,1,0,0,
        0,48,52,5,3,0,0,49,51,5,12,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,8,0,0,
        56,5,1,0,0,0,57,61,5,4,0,0,58,60,5,12,0,0,59,58,1,0,0,0,60,63,1,
        0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,
        68,5,11,0,0,65,67,5,12,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,
        0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,75,5,5,0,0,72,74,
        5,12,0,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,
        76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,11,0,0,79,7,1,0,0,0,80,84,5,
        6,0,0,81,83,5,12,0,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,
        85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,5,8,0,0,88,92,5,2,0,
        0,89,91,5,12,0,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,
        1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,10,0,0,96,100,5,2,0,
        0,97,99,5,12,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,
        101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,8,0,0,104,
        108,5,2,0,0,105,107,5,12,0,0,106,105,1,0,0,0,107,110,1,0,0,0,108,
        106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,
        112,5,8,0,0,112,116,5,2,0,0,113,115,5,12,0,0,114,113,1,0,0,0,115,
        118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,120,1,0,0,0,118,
        116,1,0,0,0,119,121,5,9,0,0,120,119,1,0,0,0,121,122,1,0,0,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,128,5,2,0,0,125,
        127,5,12,0,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,
        129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,8,0,0,132,
        133,5,7,0,0,133,9,1,0,0,0,14,22,28,36,52,61,68,75,84,92,100,108,
        116,122,128
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Paciente:'", "','", "'Diagnostico:'", 
                     "'Expede:'", "'Caduce:'", "'Medicamento:'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PALABRAS", "INT", "CONCENTRACION", "FECHA", "WS" ]

    RULE_prog = 0
    RULE_datosPacienteSentence = 1
    RULE_diagnosticoSentence = 2
    RULE_fechasSentence = 3
    RULE_medicamentoSentence = 4

    ruleNames =  [ "prog", "datosPacienteSentence", "diagnosticoSentence", 
                   "fechasSentence", "medicamentoSentence" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    PALABRAS=8
    INT=9
    CONCENTRACION=10
    FECHA=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datosPacienteSentence(self):
            return self.getTypedRuleContext(ExprParser.DatosPacienteSentenceContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def diagnosticoSentence(self):
            return self.getTypedRuleContext(ExprParser.DiagnosticoSentenceContext,0)


        def medicamentoSentence(self):
            return self.getTypedRuleContext(ExprParser.MedicamentoSentenceContext,0)


        def fechasSentence(self):
            return self.getTypedRuleContext(ExprParser.FechasSentenceContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.datosPacienteSentence()
                self.state = 11
                self.match(ExprParser.EOF)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.diagnosticoSentence()
                self.state = 14
                self.match(ExprParser.EOF)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.medicamentoSentence()
                self.state = 17
                self.match(ExprParser.EOF)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.fechasSentence()
                self.state = 20
                self.match(ExprParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatosPacienteSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALABRAS(self):
            return self.getToken(ExprParser.PALABRAS, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.WS)
            else:
                return self.getToken(ExprParser.WS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_datosPacienteSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatosPacienteSentence" ):
                listener.enterDatosPacienteSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatosPacienteSentence" ):
                listener.exitDatosPacienteSentence(self)




    def datosPacienteSentence(self):

        localctx = ExprParser.DatosPacienteSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datosPacienteSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ExprParser.T__0)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 25
                self.match(ExprParser.WS)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(ExprParser.PALABRAS)
            self.state = 32
            self.match(ExprParser.T__1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 33
                self.match(ExprParser.WS)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(ExprParser.INT)
            self.state = 40
            self.match(ExprParser.INT)
            self.state = 41
            self.match(ExprParser.INT)
            self.state = 42
            self.match(ExprParser.INT)
            self.state = 43
            self.match(ExprParser.INT)
            self.state = 44
            self.match(ExprParser.INT)
            self.state = 45
            self.match(ExprParser.INT)
            self.state = 46
            self.match(ExprParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagnosticoSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALABRAS(self):
            return self.getToken(ExprParser.PALABRAS, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.WS)
            else:
                return self.getToken(ExprParser.WS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_diagnosticoSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagnosticoSentence" ):
                listener.enterDiagnosticoSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagnosticoSentence" ):
                listener.exitDiagnosticoSentence(self)




    def diagnosticoSentence(self):

        localctx = ExprParser.DiagnosticoSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_diagnosticoSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExprParser.T__2)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 49
                self.match(ExprParser.WS)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(ExprParser.PALABRAS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FechasSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FECHA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.FECHA)
            else:
                return self.getToken(ExprParser.FECHA, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.WS)
            else:
                return self.getToken(ExprParser.WS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_fechasSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFechasSentence" ):
                listener.enterFechasSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFechasSentence" ):
                listener.exitFechasSentence(self)




    def fechasSentence(self):

        localctx = ExprParser.FechasSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fechasSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.T__3)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 58
                self.match(ExprParser.WS)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ExprParser.FECHA)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 65
                self.match(ExprParser.WS)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(ExprParser.T__4)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 72
                self.match(ExprParser.WS)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(ExprParser.FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MedicamentoSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALABRAS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PALABRAS)
            else:
                return self.getToken(ExprParser.PALABRAS, i)

        def CONCENTRACION(self):
            return self.getToken(ExprParser.CONCENTRACION, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.WS)
            else:
                return self.getToken(ExprParser.WS, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_medicamentoSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMedicamentoSentence" ):
                listener.enterMedicamentoSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMedicamentoSentence" ):
                listener.exitMedicamentoSentence(self)




    def medicamentoSentence(self):

        localctx = ExprParser.MedicamentoSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_medicamentoSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ExprParser.T__5)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 81
                self.match(ExprParser.WS)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(ExprParser.PALABRAS)
            self.state = 88
            self.match(ExprParser.T__1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 89
                self.match(ExprParser.WS)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(ExprParser.CONCENTRACION)
            self.state = 96
            self.match(ExprParser.T__1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 97
                self.match(ExprParser.WS)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(ExprParser.PALABRAS)
            self.state = 104
            self.match(ExprParser.T__1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 105
                self.match(ExprParser.WS)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(ExprParser.PALABRAS)
            self.state = 112
            self.match(ExprParser.T__1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 113
                self.match(ExprParser.WS)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.match(ExprParser.INT)
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 124
            self.match(ExprParser.T__1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 125
                self.match(ExprParser.WS)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(ExprParser.PALABRAS)
            self.state = 132
            self.match(ExprParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





