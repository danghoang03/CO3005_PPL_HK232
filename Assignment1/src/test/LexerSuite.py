import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        self.assertTrue(TestLexer.test("true false number bool string return var dynamic func for until by break continue if else elif begin end not and or","true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>",101))
        
    def test_2(self):
        self.assertTrue(TestLexer.test("+-*/%= <- != < <= > >= ... ==","+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>",102))
        
    def test_3(self):    
        self.assertTrue(TestLexer.test("[(,,)]","[,(,,,,,),],<EOF>",103))
        
    def test_4(self):
        self.assertTrue(TestLexer.test("&","Error Token &",104))
        
    def test_5(self):   
        self.assertTrue(TestLexer.test("|","Error Token |",105))
        
    def test_6(self):   
        self.assertTrue(TestLexer.test("!","Error Token !",106))
          
    def test_7(self):
        self.assertTrue(TestLexer.test("$","Error Token $",107))
        
    def test_8(self):
        self.assertTrue(TestLexer.test("@","Error Token @",108))
        
    def test_9(self):
        self.assertTrue(TestLexer.test("#","Error Token #",109))
        
    def test_10(self):
        self.assertTrue(TestLexer.test(";","Error Token ;",110))
        
    def test_11(self):
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1","A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>",111))   
          
    def test_12(self):
        self.assertTrue(TestLexer.test("12Dang","12,Dang,<EOF>",112))
        
    def test_13(self):
        self.assertTrue(TestLexer.test("05Dang","05,Dang,<EOF>",113))
        
    def test_14(self):
        self.assertTrue(TestLexer.test("Hai Dang", "Hai,Dang,<EOF>", 114))

    def test_15(self):
        self.assertTrue(TestLexer.test("if a > b then a = b + 1", "if,a,>,b,then,a,=,b,+,1,<EOF>", 115))

    def test_16(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 116))

    def test_17(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 117))

    def test_18(self):
        self.assertTrue(TestLexer.test("if 1<2 then a = b", "if,1,<,2,then,a,=,b,<EOF>", 118))

    def test_19(self):
        self.assertTrue(TestLexer.test("##This is a comment", "<EOF>", 119))
        
    def test_20(self):
        self.assertTrue(TestLexer.test("abc ##This is a comment", "abc,<EOF>", 120))
        
    def test_21(self):
        self.assertTrue(TestLexer.test("0x123", "0,x123,<EOF>", 121))

    def test_22(self):
        self.assertTrue(TestLexer.test("1.2e-3", "1.2e-3,<EOF>", 122))

    def test_23(self):
        self.assertTrue(TestLexer.test("1.2e-3.4", "1.2e-3,Error Token .", 123))

    def test_24(self):
        self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 124))

    def test_25(self):
        self.assertTrue(TestLexer.test(""" "I'm Dang" ""","I'm Dang,<EOF>", 125))

    def test_26(self):
        self.assertTrue(TestLexer.test("false abc true", "false,abc,true,<EOF>", 126))

    def test_27(self):
        self.assertTrue(TestLexer.test("(a, b, c)", "(,a,,,b,,,c,),<EOF>", 127))

    def test_28(self):
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 128))

    def test_29(self):
        self.assertTrue(TestLexer.test("]", "],<EOF>", 129))

    def test_30(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 130))

    def test_31(self):
        self.assertTrue(TestLexer.test("if else for", "if,else,for,<EOF>", 131))

    def test_32(self):
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 132))

    def test_33(self):
        self.assertTrue(TestLexer.test("a_1 b_2 c_3 d_4 e_5 f_6 g_7 h_8 i_9 j_10",
                                       "a_1,b_2,c_3,d_4,e_5,f_6,g_7,h_8,i_9,j_10,<EOF>",
                                       133))

    def test_34(self):
        self.assertTrue(TestLexer.test("array[]", "array,[,],<EOF>", 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("(1, 2, 3, 4)", "(,1,,,2,,,3,,,4,),<EOF>", 135))

    def test_36(self):
        self.assertTrue(TestLexer.test(""" "Dang '" """, """Unclosed String: Dang '" """, 136))

    def test_37(self):
        self.assertTrue(TestLexer.test(""" "Dang \'" """, """Unclosed String: Dang '" """, 137))

    def test_38(self):
        self.assertTrue(TestLexer.test(""" "Dang \\'" ""","Dang \\',<EOF>", 138))

    def test_39(self):
        self.assertTrue(TestLexer.test("0o10", "0,o10,<EOF>", 139))

    def test_40(self):
        self.assertTrue(TestLexer.test("0o18", "0,o18,<EOF>", 140))

    def test_41(self):
        self.assertTrue(TestLexer.test("0x19", "0,x19,<EOF>", 141))

    def test_42(self):
        self.assertTrue(TestLexer.test("0x1g", "0,x1g,<EOF>", 142))

    def test_43(self):
        self.assertTrue(TestLexer.test("0x", "0,x,<EOF>", 143))

    def test_44(self):
        self.assertTrue(TestLexer.test("0o", "0,o,<EOF>", 144))

    def test_45(self):
        self.assertTrue(TestLexer.test("0.", "0.,<EOF>", 145))

    def test_46(self):
        self.assertTrue(TestLexer.test(".0", "Error Token .", 146))

    def test_47(self):
        self.assertTrue(TestLexer.test("1e+5", "1e+5,<EOF>", 147))

    def test_48(self):
        self.assertTrue(TestLexer.test("1e", "1,e,<EOF>", 148))

    def test_49(self):
        self.assertTrue(TestLexer.test("1.E5", "1.E5,<EOF>", 149))

    def test_50(self):
        self.assertTrue(TestLexer.test(".1e5", "Error Token .", 150))

    def test_51(self):
        self.assertTrue(TestLexer.test("a = b + 5", "a,=,b,+,5,<EOF>", 151))

    def test_52(self):
        self.assertTrue(TestLexer.test("a = b - 5;", "a,=,b,-,5,Error Token ;", 152))

    def test_53(self):
        self.assertTrue(TestLexer.test("a = b * 5", "a,=,b,*,5,<EOF>", 153))

    def test_54(self):
        self.assertTrue(TestLexer.test("a = b / 5", "a,=,b,/,5,<EOF>", 154))

    def test_55(self):
        self.assertTrue(TestLexer.test("##Comments\n\n","\n,\n,<EOF>", 155))

    def test_56(self):
        self.assertTrue(TestLexer.test("## My name is Dang","<EOF>",156))         

    def test_57(self):
        self.assertTrue(TestLexer.test("x\n##1\ny","x,\n,\n,y,<EOF>",157))

    def test_58(self):
        self.assertTrue(TestLexer.test("###","<EOF>",158)) 

    def test_59(self):
        self.assertTrue(TestLexer.test("abc##1","abc,<EOF>",159)) 

    def test_60(self):
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",160))

    def test_61(self):
        self.assertTrue(TestLexer.test("a#","a,Error Token #",161))

    def test_62(self):
        self.assertTrue(TestLexer.test("a[12]", "a,[,12,],<EOF>", 162))

    def test_63(self):
        self.assertTrue(TestLexer.test("a[3+4]", "a,[,3,+,4,],<EOF>", 163))

    def test_64(self):
        self.assertTrue(TestLexer.test("a[3*4-1]", "a,[,3,*,4,-,1,],<EOF>", 164))

    def test_65(self):
        self.assertTrue(TestLexer.test("a[b[2]]", "a,[,b,[,2,],],<EOF>", 165))

    def test_66(self):
        self.assertTrue(TestLexer.test("a+b*c/d-e%g", "a,+,b,*,c,/,d,-,e,%,g,<EOF>", 166))

    def test_67(self):
        self.assertTrue(TestLexer.test(""" "Dang ' \\1  """, "Illegal Escape In String: Dang ' \\1", 167))                 

    def test_68(self):
        self.assertTrue(TestLexer.test(""" "Dang \\2 \\n \n """, "Illegal Escape In String: Dang \\2", 168))

    def test_69(self):
        self.assertTrue(TestLexer.test(""" "Dang '" \\123 \\n \\r """, "Illegal Escape In String: Dang '\" \\1", 169))

    def test_70(self):
        self.assertTrue(TestLexer.test(""" "Dang ' '" \\" """, "Illegal Escape In String: Dang ' '\" \\\"", 170))

    def test_71(self):
        self.assertTrue(TestLexer.test(""" "Dang \\k \\n \\r """, "Illegal Escape In String: Dang \\k", 171))

    def test_72(self):
        self.assertTrue(TestLexer.test(""" "Dang \\"1 " """, "Illegal Escape In String: Dang \\\"", 172)) 

    def test_73(self):
        self.assertTrue(TestLexer.test(""" "Dang \\' ""2 """, "Dang \\' ,Unclosed String: 2 ", 173))

    def test_74(self):
        self.assertTrue(TestLexer.test("a<=b", "a,<=,b,<EOF>", 174))

    def test_75(self):
        self.assertTrue(TestLexer.test("a and b or c", "a,and,b,or,c,<EOF>", 175))

    def test_76(self):
        self.assertTrue(TestLexer.test("a or b or c", "a,or,b,or,c,<EOF>", 176))

    def test_77(self):
        self.assertTrue(
            TestLexer.test("if (a<b)  c=d else  c=e ", "if,(,a,<,b,),c,=,d,else,c,=,e,<EOF>", 177))

    def test_78(self):
        self.assertTrue(
            TestLexer.test("if (a<b) if (b<c) c=d ", "if,(,a,<,b,),if,(,b,<,c,),c,=,d,<EOF>", 178))

    def test_79(self):
        self.assertTrue(TestLexer.test("for i until i > x by 1", "for,i,until,i,>,x,by,1,<EOF>", 179))

    def test_80(self):
        self.assertTrue(TestLexer.test("var a <- 5", "var,a,<-,5,<EOF>", 180))

    def test_81(self):
        self.assertTrue(TestLexer.test("if (a == 5) b = 6", "if,(,a,==,5,),b,=,6,<EOF>", 181))

    def test_82(self):
        self.assertTrue(TestLexer.test("a and b", "a,and,b,<EOF>", 182))

    def test_83(self):
        self.assertTrue(TestLexer.test("for i until i == n by 1", "for,i,until,i,==,n,by,1,<EOF>", 183))

    def test_84(self):
        self.assertTrue(TestLexer.test("a <- (5 + 3) * 2 - 1", "a,<-,(,5,+,3,),*,2,-,1,<EOF>", 184))

    def test_85(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang \n" """, "Unclosed String: Hai Dang ", 185))

    def test_86(self):
        self.assertTrue(TestLexer.test(""" "Hai \n Dang" """, "Unclosed String: Hai ", 186))

    def test_87(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang  """, "Unclosed String: Hai Dang  ", 187))

    def test_88(self):
        self.assertTrue(TestLexer.test(""" "Dang \\n \n """, "Unclosed String: Dang \\n ", 188))

    def test_89(self):
        self.assertTrue(TestLexer.test(""" "Dang ' \\n \\b """, "Unclosed String: Dang ' \\n \\b ", 189))

    def test_90(self):
        self.assertTrue(TestLexer.test("1.1/3", "1.1,/,3,<EOF>", 190))
    
    def test_91(self):
        self.assertTrue(TestLexer.test("+1-2","+,1,-,2,<EOF>",191)) 
    
    def test_92(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang \t \n" """, "Unclosed String: Hai Dang 	 ", 192))
    
    def test_93(self):    
        self.assertTrue(TestLexer.test(""" "Hai Dang \\" """, "Illegal Escape In String: Hai Dang \\\"", 193))
        
    def test_94(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang \\\n """, "Illegal Escape In String: Hai Dang \\\n", 194))
        
    def test_95(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang '\\ """, "Illegal Escape In String: Hai Dang '\\ ", 195))
        
    def test_96(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang \'" " """, "Hai Dang '\" ,<EOF>", 196))
        
    def test_97(self):
        self.assertTrue(TestLexer.test(""" "Hai Dang \\\'" " """, "Hai Dang \\',Unclosed String:  ", 197))
    def test_98(self):    
        self.assertTrue(TestLexer.test(
""" ##Hai Dang
##Hai Dang\n
##Hai Dang """,
"""
,
,
,<EOF>""", 198))
    def test_99(self):
        self.assertTrue(TestLexer.test(
""" ##Hai Dang "123" ## 12 \n""",
"""
,<EOF>""", 199))
    def test_100(self):    
        self.assertTrue(TestLexer.test(
""" "\\a" """,
"""Illegal Escape In String: \\a""", 200))
        