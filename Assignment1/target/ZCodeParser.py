# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u0181\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\7\2P\n\2\f\2\16\2S\13\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\\\n\3\3\4\3\4\3\4\3\4\5\4b\n\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\5\6i\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7q\n")
        buf.write("\7\3\7\3\7\5\7u\n\7\3\b\3\b\3\b\3\b\5\b{\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u0086\n\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u008c\n\13\3\13\3\13\5\13\u0090\n\13\3\13\3")
        buf.write("\13\5\13\u0094\n\13\3\13\3\13\5\13\u0098\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u009f\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00a7\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00ae\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b9")
        buf.write("\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c3")
        buf.write("\n\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00ce\n\22\3\22\3\22\3\22\3\22\5\22\u00d4\n\22\3\22\5")
        buf.write("\22\u00d7\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00de\n\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u00ed\n\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\5\27\u00f9\n\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\5\30\u0100\n\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\5\31\u0108\n\31\3\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0111\n\32\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0118\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u011f\n\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\7\35\u0127\n\35\f\35\16\35")
        buf.write("\u012a\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0132")
        buf.write("\n\36\f\36\16\36\u0135\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u013d\n\37\f\37\16\37\u0140\13\37\3 \3 \3 ")
        buf.write("\5 \u0145\n \3!\3!\3!\5!\u014a\n!\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u0150\n\"\3\"\5\"\u0153\n\"\3\"\3\"\3\"\3\"\3\"\5\"\u015a")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u0161\n#\3#\3#\3#\3#\3#\5#\u0168")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u016f\n$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\5&\u017a\n&\3\'\6\'\u017d\n\'\r\'\16\'\u017e\3\'")
        buf.write("\2\58:<(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJL\2\7\3\2\5\7\5\2\36\36 $&&\3")
        buf.write("\2\34\35\3\2\26\27\3\2\30\32\2\u0192\2Q\3\2\2\2\4[\3\2")
        buf.write("\2\2\6a\3\2\2\2\bc\3\2\2\2\nh\3\2\2\2\fj\3\2\2\2\16z\3")
        buf.write("\2\2\2\20|\3\2\2\2\22\u0081\3\2\2\2\24\u0087\3\2\2\2\26")
        buf.write("\u009e\3\2\2\2\30\u00a0\3\2\2\2\32\u00ad\3\2\2\2\34\u00b8")
        buf.write("\3\2\2\2\36\u00ba\3\2\2\2 \u00bd\3\2\2\2\"\u00c8\3\2\2")
        buf.write("\2$\u00e3\3\2\2\2&\u00e5\3\2\2\2(\u00f0\3\2\2\2*\u00f3")
        buf.write("\3\2\2\2,\u00f6\3\2\2\2.\u00fc\3\2\2\2\60\u0104\3\2\2")
        buf.write("\2\62\u0110\3\2\2\2\64\u0117\3\2\2\2\66\u011e\3\2\2\2")
        buf.write("8\u0120\3\2\2\2:\u012b\3\2\2\2<\u0136\3\2\2\2>\u0144\3")
        buf.write("\2\2\2@\u0149\3\2\2\2B\u0159\3\2\2\2D\u0167\3\2\2\2F\u016e")
        buf.write("\3\2\2\2H\u0170\3\2\2\2J\u0179\3\2\2\2L\u017c\3\2\2\2")
        buf.write("NP\7/\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3")
        buf.write("\2\2\2SQ\3\2\2\2TU\5\4\3\2UV\7\2\2\3V\3\3\2\2\2WX\5\6")
        buf.write("\4\2XY\5\4\3\2Y\\\3\2\2\2Z\\\5\6\4\2[W\3\2\2\2[Z\3\2\2")
        buf.write("\2\\\5\3\2\2\2]b\5\24\13\2^_\5\n\6\2_`\5L\'\2`b\3\2\2")
        buf.write("\2a]\3\2\2\2a^\3\2\2\2b\7\3\2\2\2cd\t\2\2\2d\t\3\2\2\2")
        buf.write("ei\5\f\7\2fi\5\20\t\2gi\5\22\n\2he\3\2\2\2hf\3\2\2\2h")
        buf.write("g\3\2\2\2i\13\3\2\2\2jk\5\b\5\2kp\7,\2\2lm\7)\2\2mn\5")
        buf.write("\16\b\2no\7*\2\2oq\3\2\2\2pl\3\2\2\2pq\3\2\2\2qt\3\2\2")
        buf.write("\2rs\7\37\2\2su\5\64\33\2tr\3\2\2\2tu\3\2\2\2u\r\3\2\2")
        buf.write("\2vw\7-\2\2wx\7+\2\2x{\5\16\b\2y{\7-\2\2zv\3\2\2\2zy\3")
        buf.write("\2\2\2{\17\3\2\2\2|}\7\t\2\2}~\7,\2\2~\177\7\37\2\2\177")
        buf.write("\u0080\5\64\33\2\u0080\21\3\2\2\2\u0081\u0082\7\n\2\2")
        buf.write("\u0082\u0085\7,\2\2\u0083\u0084\7\37\2\2\u0084\u0086\5")
        buf.write("\64\33\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\23\3\2\2\2\u0087\u0088\7\13\2\2\u0088\u0089\7,\2\2\u0089")
        buf.write("\u008b\7\'\2\2\u008a\u008c\5\26\f\2\u008b\u008a\3\2\2")
        buf.write("\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0097")
        buf.write("\7(\2\2\u008e\u0090\5L\'\2\u008f\u008e\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0098\5,\27\2\u0092")
        buf.write("\u0094\5L\'\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0098\5\60\31\2\u0096\u0098")
        buf.write("\5L\'\2\u0097\u008f\3\2\2\2\u0097\u0093\3\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\25\3\2\2\2\u0099\u009a\5\30\r\2\u009a")
        buf.write("\u009b\7+\2\2\u009b\u009c\5\26\f\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009f\5\30\r\2\u009e\u0099\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\27\3\2\2\2\u00a0\u00a1\5\b\5\2\u00a1\u00a6")
        buf.write("\7,\2\2\u00a2\u00a3\7)\2\2\u00a3\u00a4\5\16\b\2\u00a4")
        buf.write("\u00a5\7*\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a2\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\31\3\2\2\2\u00a8\u00ae\5\64")
        buf.write("\33\2\u00a9\u00aa\5\64\33\2\u00aa\u00ab\7+\2\2\u00ab\u00ac")
        buf.write("\5\32\16\2\u00ac\u00ae\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad")
        buf.write("\u00a9\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00b9\5\36\20\2")
        buf.write("\u00b0\u00b9\5 \21\2\u00b1\u00b9\5\"\22\2\u00b2\u00b9")
        buf.write("\5&\24\2\u00b3\u00b9\5(\25\2\u00b4\u00b9\5*\26\2\u00b5")
        buf.write("\u00b9\5,\27\2\u00b6\u00b9\5.\30\2\u00b7\u00b9\5\60\31")
        buf.write("\2\u00b8\u00af\3\2\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b1")
        buf.write("\3\2\2\2\u00b8\u00b2\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8")
        buf.write("\u00b4\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b7\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00bb\5\n")
        buf.write("\6\2\u00bb\u00bc\5L\'\2\u00bc\37\3\2\2\2\u00bd\u00c2\7")
        buf.write(",\2\2\u00be\u00bf\7)\2\2\u00bf\u00c0\5J&\2\u00c0\u00c1")
        buf.write("\7*\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00be\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7\37\2")
        buf.write("\2\u00c5\u00c6\5\64\33\2\u00c6\u00c7\5L\'\2\u00c7!\3\2")
        buf.write("\2\2\u00c8\u00c9\7\21\2\2\u00c9\u00ca\7\'\2\2\u00ca\u00cb")
        buf.write("\5\64\33\2\u00cb\u00cd\7(\2\2\u00cc\u00ce\5L\'\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\5\34\17\2\u00d0\u00d6\5$\23\2\u00d1\u00d3")
        buf.write("\7\22\2\2\u00d2\u00d4\5L\'\2\u00d3\u00d2\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\5\34\17")
        buf.write("\2\u00d6\u00d1\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7#\3\2")
        buf.write("\2\2\u00d8\u00d9\7\23\2\2\u00d9\u00da\7\'\2\2\u00da\u00db")
        buf.write("\5\64\33\2\u00db\u00dd\7(\2\2\u00dc\u00de\5L\'\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e0\5\34\17\2\u00e0\u00e1\5$\23\2\u00e1\u00e4")
        buf.write("\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00d8\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\7\f\2\2\u00e6")
        buf.write("\u00e7\7,\2\2\u00e7\u00e8\7\r\2\2\u00e8\u00e9\5\64\33")
        buf.write("\2\u00e9\u00ea\7\16\2\2\u00ea\u00ec\5\64\33\2\u00eb\u00ed")
        buf.write("\5L\'\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00ef\5\34\17\2\u00ef\'\3\2\2\2\u00f0")
        buf.write("\u00f1\7\17\2\2\u00f1\u00f2\5L\'\2\u00f2)\3\2\2\2\u00f3")
        buf.write("\u00f4\7\20\2\2\u00f4\u00f5\5L\'\2\u00f5+\3\2\2\2\u00f6")
        buf.write("\u00f8\7\b\2\2\u00f7\u00f9\5\64\33\2\u00f8\u00f7\3\2\2")
        buf.write("\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb")
        buf.write("\5L\'\2\u00fb-\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd\u00ff")
        buf.write("\7\'\2\2\u00fe\u0100\5J&\2\u00ff\u00fe\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7(\2\2\u0102")
        buf.write("\u0103\5L\'\2\u0103/\3\2\2\2\u0104\u0105\7\24\2\2\u0105")
        buf.write("\u0107\5L\'\2\u0106\u0108\5\62\32\2\u0107\u0106\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write("\7\25\2\2\u010a\u010b\5L\'\2\u010b\61\3\2\2\2\u010c\u010d")
        buf.write("\5\34\17\2\u010d\u010e\5\62\32\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u0111\5\34\17\2\u0110\u010c\3\2\2\2\u0110\u010f\3\2\2")
        buf.write("\2\u0111\63\3\2\2\2\u0112\u0113\5\66\34\2\u0113\u0114")
        buf.write("\7%\2\2\u0114\u0115\5\66\34\2\u0115\u0118\3\2\2\2\u0116")
        buf.write("\u0118\5\66\34\2\u0117\u0112\3\2\2\2\u0117\u0116\3\2\2")
        buf.write("\2\u0118\65\3\2\2\2\u0119\u011a\58\35\2\u011a\u011b\t")
        buf.write("\3\2\2\u011b\u011c\58\35\2\u011c\u011f\3\2\2\2\u011d\u011f")
        buf.write("\58\35\2\u011e\u0119\3\2\2\2\u011e\u011d\3\2\2\2\u011f")
        buf.write("\67\3\2\2\2\u0120\u0121\b\35\1\2\u0121\u0122\5:\36\2\u0122")
        buf.write("\u0128\3\2\2\2\u0123\u0124\f\4\2\2\u0124\u0125\t\4\2\2")
        buf.write("\u0125\u0127\5:\36\2\u0126\u0123\3\2\2\2\u0127\u012a\3")
        buf.write("\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u01299")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\b\36\1\2\u012c")
        buf.write("\u012d\5<\37\2\u012d\u0133\3\2\2\2\u012e\u012f\f\4\2\2")
        buf.write("\u012f\u0130\t\5\2\2\u0130\u0132\5<\37\2\u0131\u012e\3")
        buf.write("\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134;\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137")
        buf.write("\b\37\1\2\u0137\u0138\5> \2\u0138\u013e\3\2\2\2\u0139")
        buf.write("\u013a\f\4\2\2\u013a\u013b\t\6\2\2\u013b\u013d\5> \2\u013c")
        buf.write("\u0139\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f=\3\2\2\2\u0140\u013e\3\2\2")
        buf.write("\2\u0141\u0142\7\33\2\2\u0142\u0145\5> \2\u0143\u0145")
        buf.write("\5@!\2\u0144\u0141\3\2\2\2\u0144\u0143\3\2\2\2\u0145?")
        buf.write("\3\2\2\2\u0146\u0147\t\5\2\2\u0147\u014a\5@!\2\u0148\u014a")
        buf.write("\5B\"\2\u0149\u0146\3\2\2\2\u0149\u0148\3\2\2\2\u014a")
        buf.write("A\3\2\2\2\u014b\u0153\7,\2\2\u014c\u014d\7,\2\2\u014d")
        buf.write("\u014f\7\'\2\2\u014e\u0150\5\32\16\2\u014f\u014e\3\2\2")
        buf.write("\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153")
        buf.write("\7(\2\2\u0152\u014b\3\2\2\2\u0152\u014c\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0155\7)\2\2\u0155\u0156\5\32\16")
        buf.write("\2\u0156\u0157\7*\2\2\u0157\u015a\3\2\2\2\u0158\u015a")
        buf.write("\5D#\2\u0159\u0152\3\2\2\2\u0159\u0158\3\2\2\2\u015aC")
        buf.write("\3\2\2\2\u015b\u0168\5F$\2\u015c\u0168\7,\2\2\u015d\u015e")
        buf.write("\7,\2\2\u015e\u0160\7\'\2\2\u015f\u0161\5J&\2\u0160\u015f")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0168\7(\2\2\u0163\u0164\7\'\2\2\u0164\u0165\5\64\33")
        buf.write("\2\u0165\u0166\7(\2\2\u0166\u0168\3\2\2\2\u0167\u015b")
        buf.write("\3\2\2\2\u0167\u015c\3\2\2\2\u0167\u015d\3\2\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0168E\3\2\2\2\u0169\u016f\7-\2\2\u016a")
        buf.write("\u016f\7.\2\2\u016b\u016f\7\3\2\2\u016c\u016f\7\4\2\2")
        buf.write("\u016d\u016f\5H%\2\u016e\u0169\3\2\2\2\u016e\u016a\3\2")
        buf.write("\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016fG\3\2\2\2\u0170\u0171\7)\2\2\u0171\u0172")
        buf.write("\5J&\2\u0172\u0173\7*\2\2\u0173I\3\2\2\2\u0174\u0175\5")
        buf.write("\64\33\2\u0175\u0176\7+\2\2\u0176\u0177\5J&\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u017a\5\64\33\2\u0179\u0174\3\2\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017aK\3\2\2\2\u017b\u017d\7/\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017fM\3\2\2\2,Q[ahptz\u0085\u008b")
        buf.write("\u008f\u0093\u0097\u009e\u00a6\u00ad\u00b8\u00c2\u00cd")
        buf.write("\u00d3\u00d6\u00dd\u00e3\u00ec\u00f8\u00ff\u0107\u0110")
        buf.write("\u0117\u011e\u0128\u0133\u013e\u0144\u0149\u014f\u0152")
        buf.write("\u0159\u0160\u0167\u016e\u0179\u017e")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT_OP", 
                      "AND_OP", "OR_OP", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "SMALLER", "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "CONCAT", "EQUAL_STRING", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", "IDENTIFIER", 
                      "NUM_LIT", "STRING_LIT", "NEWLINE", "COMMENTS", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_typ = 3
    RULE_variables = 4
    RULE_keyword_var = 5
    RULE_list_number_lit = 6
    RULE_implicit_var = 7
    RULE_implicit_dynamic = 8
    RULE_function = 9
    RULE_param_list = 10
    RULE_param_declaration = 11
    RULE_index_operator = 12
    RULE_statement = 13
    RULE_declaration_statement = 14
    RULE_assignment_statement = 15
    RULE_if_statement = 16
    RULE_elif_list = 17
    RULE_for_statement = 18
    RULE_break_statement = 19
    RULE_continue_statement = 20
    RULE_return_statement = 21
    RULE_call_statement = 22
    RULE_block_statement = 23
    RULE_block_list = 24
    RULE_expression = 25
    RULE_expression1 = 26
    RULE_expression2 = 27
    RULE_expression3 = 28
    RULE_expression4 = 29
    RULE_expression5 = 30
    RULE_expression6 = 31
    RULE_expression7 = 32
    RULE_expression8 = 33
    RULE_literals = 34
    RULE_array_lit = 35
    RULE_expression_list = 36
    RULE_ignore = 37

    ruleNames =  [ "program", "list_declared", "declared", "typ", "variables", 
                   "keyword_var", "list_number_lit", "implicit_var", "implicit_dynamic", 
                   "function", "param_list", "param_declaration", "index_operator", 
                   "statement", "declaration_statement", "assignment_statement", 
                   "if_statement", "elif_list", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "block_statement", "block_list", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "literals", 
                   "array_lit", "expression_list", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    NOT_OP=25
    AND_OP=26
    OR_OP=27
    EQUAL=28
    ASSIGN=29
    NOT_EQUAL=30
    SMALLER=31
    SMALLER_EQUAL=32
    GREATER=33
    GREATER_EQUAL=34
    CONCAT=35
    EQUAL_STRING=36
    OPEN_PAREN=37
    CLOSE_PAREN=38
    OPEN_BRACKET=39
    CLOSE_BRACKET=40
    COMMA=41
    IDENTIFIER=42
    NUM_LIT=43
    STRING_LIT=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 76
                self.match(ZCodeParser.NEWLINE)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.list_declared()
            self.state = 83
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declared()
                self.state = 86
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.variables()
                self.state = 93
                self.ignore()
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variables)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.keyword_var()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.implicit_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.implicit_dynamic()
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


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def list_number_lit(self):
            return self.getTypedRuleContext(ZCodeParser.List_number_litContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.typ()
            self.state = 105
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OPEN_BRACKET:
                self.state = 106
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 107
                self.list_number_lit()
                self.state = 108
                self.match(ZCodeParser.CLOSE_BRACKET)


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 112
                self.match(ZCodeParser.ASSIGN)
                self.state = 113
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_number_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_number_lit(self):
            return self.getTypedRuleContext(ZCodeParser.List_number_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_number_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_number_lit" ):
                return visitor.visitList_number_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_number_lit(self):

        localctx = ZCodeParser.List_number_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_number_lit)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(ZCodeParser.NUM_LIT)
                self.state = 117
                self.match(ZCodeParser.COMMA)
                self.state = 118
                self.list_number_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ZCodeParser.VAR)
            self.state = 123
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 124
            self.match(ZCodeParser.ASSIGN)
            self.state = 125
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ZCodeParser.DYNAMIC)
            self.state = 128
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 129
                self.match(ZCodeParser.ASSIGN)
                self.state = 130
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.FUNC)
            self.state = 134
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 135
            self.match(ZCodeParser.OPEN_PAREN)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 136
                self.param_list()


            self.state = 139
            self.match(ZCodeParser.CLOSE_PAREN)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 140
                    self.ignore()


                self.state = 143
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 144
                    self.ignore()


                self.state = 147
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 148
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declarationContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.param_declaration()
                self.state = 152
                self.match(ZCodeParser.COMMA)
                self.state = 153
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.param_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def list_number_lit(self):
            return self.getTypedRuleContext(ZCodeParser.List_number_litContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_declaration" ):
                return visitor.visitParam_declaration(self)
            else:
                return visitor.visitChildren(self)




    def param_declaration(self):

        localctx = ZCodeParser.Param_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.typ()
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OPEN_BRACKET:
                self.state = 160
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 161
                self.list_number_lit()
                self.state = 162
                self.match(ZCodeParser.CLOSE_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_index_operator)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.expression()
                self.state = 168
                self.match(ZCodeParser.COMMA)
                self.state = 169
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 177
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 179
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 180
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 181
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.variables()
            self.state = 185
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OPEN_BRACKET:
                self.state = 188
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 189
                self.expression_list()
                self.state = 190
                self.match(ZCodeParser.CLOSE_BRACKET)


            self.state = 194
            self.match(ZCodeParser.ASSIGN)
            self.state = 195
            self.expression()
            self.state = 196
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ZCodeParser.IF)
            self.state = 199
            self.match(ZCodeParser.OPEN_PAREN)
            self.state = 200
            self.expression()
            self.state = 201
            self.match(ZCodeParser.CLOSE_PAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 202
                self.ignore()


            self.state = 205
            self.statement()
            self.state = 206
            self.elif_list()
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 207
                self.match(ZCodeParser.ELSE)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 208
                    self.ignore()


                self.state = 211
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elif_list)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.ELIF)
                self.state = 215
                self.match(ZCodeParser.OPEN_PAREN)
                self.state = 216
                self.expression()
                self.state = 217
                self.match(ZCodeParser.CLOSE_PAREN)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 218
                    self.ignore()


                self.state = 221
                self.statement()
                self.state = 222
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(ZCodeParser.FOR)
            self.state = 228
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 229
            self.match(ZCodeParser.UNTIL)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(ZCodeParser.BY)
            self.state = 232
            self.expression()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 233
                self.ignore()


            self.state = 236
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ZCodeParser.BREAK)
            self.state = 239
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.CONTINUE)
            self.state = 242
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.RETURN)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.OPEN_PAREN) | (1 << ZCodeParser.OPEN_BRACKET) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 245
                self.expression()


            self.state = 248
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 251
            self.match(ZCodeParser.OPEN_PAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.OPEN_PAREN) | (1 << ZCodeParser.OPEN_BRACKET) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 252
                self.expression_list()


            self.state = 255
            self.match(ZCodeParser.CLOSE_PAREN)
            self.state = 256
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def block_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.BEGIN)
            self.state = 259
            self.ignore()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 260
                self.block_list()


            self.state = 263
            self.match(ZCodeParser.END)
            self.state = 264
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def block_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_list" ):
                return visitor.visitBlock_list(self)
            else:
                return visitor.visitChildren(self)




    def block_list(self):

        localctx = ZCodeParser.Block_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_list)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.statement()
                self.state = 267
                self.block_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.expression1()
                self.state = 273
                self.match(ZCodeParser.CONCAT)
                self.state = 274
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EQUAL_STRING(self):
            return self.getToken(ZCodeParser.EQUAL_STRING, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def SMALLER(self):
            return self.getToken(ZCodeParser.SMALLER, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def SMALLER_EQUAL(self):
            return self.getToken(ZCodeParser.SMALLER_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expression2(0)
                self.state = 280
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.SMALLER) | (1 << ZCodeParser.SMALLER_EQUAL) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GREATER_EQUAL) | (1 << ZCodeParser.EQUAL_STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND_OP(self):
            return self.getToken(ZCodeParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(ZCodeParser.OR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 291
                    self.expression3(0) 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 302
                    self.expression4(0) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.expression5() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(ZCodeParser.NOT_OP, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression5)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(ZCodeParser.NOT_OP)
                self.state = 320
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.OPEN_PAREN, ZCodeParser.OPEN_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.expression6()
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 325
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPEN_PAREN, ZCodeParser.OPEN_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def index_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Index_operatorContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,i)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 330
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 331
                    self.match(ZCodeParser.OPEN_PAREN)
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.OPEN_PAREN) | (1 << ZCodeParser.OPEN_BRACKET) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                        self.state = 332
                        self.index_operator()


                    self.state = 335
                    self.match(ZCodeParser.CLOSE_PAREN)
                    pass


                self.state = 338
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 339
                self.index_operator()
                self.state = 340
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.expression8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(ZCodeParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ZCodeParser.CLOSE_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression8)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 348
                self.match(ZCodeParser.OPEN_PAREN)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.OPEN_PAREN) | (1 << ZCodeParser.OPEN_BRACKET) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                    self.state = 349
                    self.expression_list()


                self.state = 352
                self.match(ZCodeParser.CLOSE_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.match(ZCodeParser.OPEN_PAREN)
                self.state = 354
                self.expression()
                self.state = 355
                self.match(ZCodeParser.CLOSE_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literals)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.array_lit()
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.OPEN_BRACKET)
            self.state = 367
            self.expression_list()
            self.state = 368
            self.match(ZCodeParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression_list)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.expression()
                self.state = 371
                self.match(ZCodeParser.COMMA)
                self.state = 372
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 377
                self.match(ZCodeParser.NEWLINE)
                self.state = 380 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expression2_sempred
        self._predicates[28] = self.expression3_sempred
        self._predicates[29] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




