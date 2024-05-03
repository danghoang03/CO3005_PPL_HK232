import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_1(self):    
        input = """ 
            number a
            
            ## This is comment
            number b <- 0
            bool arr1[1,2]
            bool arr2[1,2] <- 1 + 1 / 2 * 3
            string c[3]
            ## This is comment
            
            string d[5] <- 2 ... " tring"
            var x <- 0
            dynamic y
            dynamic z <- 0
            ## This is comment
             
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, NumLit(0.0)), VarDecl(Id(arr1), ArrayType([1.0, 2.0], BoolType), None, None), VarDecl(Id(arr2), ArrayType([1.0, 2.0], BoolType), None, BinaryOp(+, NumLit(1.0), BinaryOp(*, BinaryOp(/, NumLit(1.0), NumLit(2.0)), NumLit(3.0)))), VarDecl(Id(c), ArrayType([3.0], StringType), None, None), VarDecl(Id(d), ArrayType([5.0], StringType), None, BinaryOp(..., NumLit(2.0), StringLit( tring))), VarDecl(Id(x), None, var, NumLit(0.0)), VarDecl(Id(y), None, dynamic, None), VarDecl(Id(z), None, dynamic, NumLit(0.0))])"""
        self.assertTrue(TestAST.test(input, expect, 301))   
    
    def test_2(self):    
        input = """ 
            var a <- 1
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 302))   
    
    def test_3(self):   
        input = """ 
            number a[5] <- 3
        """
        expect = """Program([VarDecl(Id(a), ArrayType([5.0], NumberType), None, NumLit(3.0))])"""
        self.assertTrue(TestAST.test(input, expect, 303))         

    def test_4(self):
        input = """ 
            bool c <- b[1+2]
        """
        expect = """Program([VarDecl(Id(c), BoolType, None, ArrayCell(Id(b), [BinaryOp(+, NumLit(1.0), NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 304))   
    
    def test_5(self):    
        input = """ 
            bool a[1,2]
        """
        expect = """Program([VarDecl(Id(a), ArrayType([1.0, 2.0], BoolType), None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 305)) 

    def test_6(self):
        input = """ 
            string a[1]
        """
        expect = """Program([VarDecl(Id(a), ArrayType([1.0], StringType), None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 306))  
        
    def test_7(self):
        input = """ 
            bool a[1]
        """
        expect = """Program([VarDecl(Id(a), ArrayType([1.0], BoolType), None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_8(self):
        input = """ 
            var a <- 7
            number b <- 5
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(7.0)), VarDecl(Id(b), NumberType, None, NumLit(5.0))])"""
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_9(self):
        input = """ 
            var a <- 6
            number b 
            dynamic c
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(6.0)), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), None, dynamic, None)])"""
        self.assertTrue(TestAST.test(input, expect, 309)) 
        
    def test_10(self):
        input = """ 
            var a <- 6
            number b <- 5
            dynamic c
            var d <- 1
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(6.0)), VarDecl(Id(b), NumberType, None, NumLit(5.0)), VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 310)) 
        
    def test_11(self):
        input = """ 
            func main()
            func main(number a[2],bool b[1,2,3], bool c[1,2,3], string s, bool d)
            func main(number num1, number num2)
                var t <- 1
            func main(number y)
        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([2.0], NumberType), None, None), VarDecl(Id(b), ArrayType([1.0, 2.0, 3.0], BoolType), None, None), VarDecl(Id(c), ArrayType([1.0, 2.0, 3.0], BoolType), None, None), VarDecl(Id(s), StringType, None, None), VarDecl(Id(d), BoolType, None, None)], None), FuncDecl(Id(main), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], None), VarDecl(Id(t), None, var, NumLit(1.0)), FuncDecl(Id(main), [VarDecl(Id(y), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 311))       
    
    def test_12(self):    
        input = """ 
            func main()
            ## This is comment
            func foo(number a) ## This is comment
        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 312))  

    def test_13(self):
        input = """ 
            func main(number a)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_14(self):    
        input = """ 
            func main(string a[2,3])
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([2.0, 3.0], StringType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 314))     
        
    def test_15(self):    
        input = """ 
            func main(number a, bool b)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), BoolType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 315))    
        
    def test_16(self):    
        input = """ 
            func main(number a[2,3], string b[4,5])
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, None), VarDecl(Id(b), ArrayType([4.0, 5.0], StringType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_17(self):    
        input = """ 
            func main(number a[2])
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([2.0], NumberType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_18(self):    
        input = """ 
            func main(number a, string b, bool c)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None), VarDecl(Id(c), BoolType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 318))       
        
    def test_19(self):    
        input = """ 
            func main(number a , bool b, string s)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), BoolType, None, None), VarDecl(Id(s), StringType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test_20(self):    
        input = """ 
            func main(number a[5], number b)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 320))  
        
    def test_21(self):
        input = """ 
            ##This is comment
            ##This is comment
            
            func main(number a)
            begin
                var c <- 1
            end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(c), None, var, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 321))   
    
    def test_22(self):    
        input = """ 
            func main(string a) 
                begin 
                    break ## This is comment
                end
            func main(number a) 
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), StringType, None, None)], Block([Break])), FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 322))    

    def test_23(self):
        input = """ 
            func main(number a[1,2,3]) ##This is comment
            begin
                number a <- 1 + 2
            end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, None)], Block([VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), NumLit(2.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 323))    
    
    def test_24(self):
        input = """ 
            ##This is comment
            ##This is comment
            
            func main(number a)
            begin
            var c <- 1 ##Declare variable
            end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(c), None, var, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test_25(self):    
        input = """ 
            ##This is comment
            func main(number a) 
                ##This is comment
                
                begin 
                    break
                end
                
                ##This is comment
                ##This is comment
            func main(number a)
            ##This is comment        
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Break])), FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 325))                  

    def test_26(self):
        input = """ 
            ## This is comment
            
            var a <- 1 ## This is comment
            ## This is comment
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 326))   
    
    def test_27(self):    
        input = """var a <- 1
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 327))  

    def test_28(self):
        input = """func main(number a) 
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 328))  
        
    def test_29(self):
        input = """
            func main(number a) 
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 329)) 
        
    def test_30(self):
        input = """var a <- 1 ## This is comment
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 330)) 
    
    def test_31(self):
        input = """ var str <- "Hai" ... "Dang" 
        """
        expect = """Program([VarDecl(Id(str), None, var, BinaryOp(..., StringLit(Hai), StringLit(Dang)))])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    
    def test_32(self):    
        input = """ var str <- "Hai" and "Dang" 
        """
        expect = """Program([VarDecl(Id(str), None, var, BinaryOp(and, StringLit(Hai), StringLit(Dang)))])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_33(self):    
        input = """ 
            var a <- 4 > 5 
            var b <- 1 >= 2
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(>, NumLit(4.0), NumLit(5.0))), VarDecl(Id(b), None, var, BinaryOp(>=, NumLit(1.0), NumLit(2.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_34(self):
        input = """
            var a <- 4 >= 5
            var b <- 1 >= 2
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(>=, NumLit(4.0), NumLit(5.0))), VarDecl(Id(b), None, var, BinaryOp(>=, NumLit(1.0), NumLit(2.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
        
    def test_35(self):
        input = """ var a <- true > x
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(>, BooleanLit(True), Id(x)))])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
        
    def test_36(self):
        input = """
            func findMax(number a, number b)
            begin
            if (0 < (a < b))
                return b
            else
                return a
            end
        """
        expect = """Program([FuncDecl(Id(findMax), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(<, NumLit(0.0), BinaryOp(<, Id(a), Id(b))), Return(Id(b))), [], Return(Id(a)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_37(self):
        input = """
            func findMax(number a, number b)
            begin
            if (a < b)
                return b
            else
                return a
            end
        """
        expect = """Program([FuncDecl(Id(findMax), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(<, Id(a), Id(b)), Return(Id(b))), [], Return(Id(a)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 337))  
        
    def test_38(self):
        input = """
            func concatString(string a, string b, string c)
                return (a ... b)
        """
        expect = """Program([FuncDecl(Id(concatString), [VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, None), VarDecl(Id(c), StringType, None, None)], Return(BinaryOp(..., Id(a), Id(b))))])"""
        self.assertTrue(TestAST.test(input, expect, 338)) 
        
    def test_39(self):
        input = """
            func concatString(string a, string b)
                return (a ... b)
        """
        expect = """Program([FuncDecl(Id(concatString), [VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, None)], Return(BinaryOp(..., Id(a), Id(b))))])"""
        self.assertTrue(TestAST.test(input, expect, 339)) 
              
    def test_40(self):
        input = """
            var a <- 2 > 3
            var b <- "hello" >= "hi"
            var c <- "hello" < 5
            var d <- 12 <= 10
            var e <- "string" == "hello"
            var f <- 3 = 4
            var g <- 1 >= 2 ... 1 > 2
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(>, NumLit(2.0), NumLit(3.0))), VarDecl(Id(b), None, var, BinaryOp(>=, StringLit(hello), StringLit(hi))), VarDecl(Id(c), None, var, BinaryOp(<, StringLit(hello), NumLit(5.0))), VarDecl(Id(d), None, var, BinaryOp(<=, NumLit(12.0), NumLit(10.0))), VarDecl(Id(e), None, var, BinaryOp(==, StringLit(string), StringLit(hello))), VarDecl(Id(f), None, var, BinaryOp(=, NumLit(3.0), NumLit(4.0))), VarDecl(Id(g), None, var, BinaryOp(..., BinaryOp(>=, NumLit(1.0), NumLit(2.0)), BinaryOp(>, NumLit(1.0), NumLit(2.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 340)) 

    def test_41(self):
        input = """ 
            var a <- 1 + 2
            number b <- 1 + 2 + 3 -4 + 5
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, NumLit(1.0), NumLit(2.0))), VarDecl(Id(b), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), NumLit(4.0)), NumLit(5.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_42(self):
        input = """ 
            number a <- 1 * 2 / 3 + 4 - 7
            number b <- 2 + 1 * 8 - 14 / 3
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), NumLit(4.0)), NumLit(7.0))), VarDecl(Id(b), NumberType, None, BinaryOp(-, BinaryOp(+, NumLit(2.0), BinaryOp(*, NumLit(1.0), NumLit(8.0))), BinaryOp(/, NumLit(14.0), NumLit(3.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_43(self):
        input = """ 
            var a <- x and y or z
            var b <- x or y or z
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(or, BinaryOp(and, Id(x), Id(y)), Id(z))), VarDecl(Id(b), None, var, BinaryOp(or, BinaryOp(or, Id(x), Id(y)), Id(z)))])"""
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_44(self):
        input = """ 
            var a <- x and y and z
            var b <- x == y or y + 1
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(and, BinaryOp(and, Id(x), Id(y)), Id(z))), VarDecl(Id(b), None, var, BinaryOp(==, Id(x), BinaryOp(or, Id(y), BinaryOp(+, Id(y), NumLit(1.0)))))])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    
    def test_45(self):            
        input = """var a <- 2 >= 1 and 1 + 2
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(>=, NumLit(2.0), BinaryOp(and, NumLit(1.0), BinaryOp(+, NumLit(1.0), NumLit(2.0)))))])"""
        self.assertTrue(TestAST.test(input, expect, 345)) 
        
    def test_46(self):  
        input = """ 
            var a <- -1 + 2
            var b <- not not not a
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, UnaryOp(-, NumLit(1.0)), NumLit(2.0))), VarDecl(Id(b), None, var, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(a)))))])"""
        self.assertTrue(TestAST.test(input, expect, 346)) 
    
    def test_47(self):
        input = """var a <- -1
        """
        expect = """Program([VarDecl(Id(a), None, var, UnaryOp(-, NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 347)) 

    def test_48(self):
        input = """var VoTien <- - (not 1)
        """
        expect = """Program([VarDecl(Id(VoTien), None, var, UnaryOp(-, UnaryOp(not, NumLit(1.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 348)) 
        
    def test_49(self):
        input = """var a <- not not not not - - - - 1
        """
        expect = """Program([VarDecl(Id(a), None, var, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))))])"""
        self.assertTrue(TestAST.test(input, expect, 349)) 
        
    def test_50(self):
        input = """var a <- not 1
        """
        expect = """Program([VarDecl(Id(a), None, var, UnaryOp(not, NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 350)) 
        
    def test_51(self):
        input = """ var a <- arr[1] + 1
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, ArrayCell(Id(arr), [NumLit(1.0)]), NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_52(self):    
        input = """var a <- arr[1,2] + b[[1],[1]]
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0)]), ArrayCell(Id(b), [ArrayLit(NumLit(1.0)), ArrayLit(NumLit(1.0))])))])"""
        self.assertTrue(TestAST.test(input, expect, 352)) 

    def test_53(self):    
        input = """var a <- arr[1,2] + getArr()[1]
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0)]), ArrayCell(CallExpr(Id(getArr), []), [NumLit(1.0)])))])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_54(self):    
        input = """var a <- arr[1,2] + b[[1],[1]]
        """
        expect = """Program([VarDecl(Id(a), None, var, BinaryOp(+, ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0)]), ArrayCell(Id(b), [ArrayLit(NumLit(1.0)), ArrayLit(NumLit(1.0))])))])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_55(self):
        input = """ 
            var a <- func1()
            var b <- func2(1,2)
            var c <- func3(x,array[1])[2]
            var d <- func4(x,str[3] ... "hi")[1,2]
        """
        expect = """Program([VarDecl(Id(a), None, var, CallExpr(Id(func1), [])), VarDecl(Id(b), None, var, CallExpr(Id(func2), [NumLit(1.0), NumLit(2.0)])), VarDecl(Id(c), None, var, ArrayCell(CallExpr(Id(func3), [Id(x), ArrayCell(Id(array), [NumLit(1.0)])]), [NumLit(2.0)])), VarDecl(Id(d), None, var, ArrayCell(CallExpr(Id(func4), [Id(x), BinaryOp(..., ArrayCell(Id(str), [NumLit(3.0)]), StringLit(hi))]), [NumLit(1.0), NumLit(2.0)]))])"""
        self.assertTrue(TestAST.test(input, expect, 355))    

    def test_56(self):
        input = """ 
            var x <- func1() + -1 / 2 * 3 < 4 ... "string" > "hi"
            number arr[5] <-  [1, 2, 3, 4, 5] + [[1, 2 + 5 * 2 / 1, 2], [4, 5, 6]]
        """
        expect = """Program([VarDecl(Id(x), None, var, BinaryOp(..., BinaryOp(<, BinaryOp(+, CallExpr(Id(func1), []), BinaryOp(*, BinaryOp(/, UnaryOp(-, NumLit(1.0)), NumLit(2.0)), NumLit(3.0))), NumLit(4.0)), BinaryOp(>, StringLit(string), StringLit(hi)))), VarDecl(Id(arr), ArrayType([5.0], NumberType), None, BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), ArrayLit(ArrayLit(NumLit(1.0), BinaryOp(+, NumLit(2.0), BinaryOp(/, BinaryOp(*, NumLit(5.0), NumLit(2.0)), NumLit(1.0))), NumLit(2.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))))])"""
        self.assertTrue(TestAST.test(input, expect, 356))  
        
    def test_57(self):
        input = """ 
            var x <- func1(a,arr[2,3] ... "hello")[1]
            var y <- (str1 ... str2) + b and (a >= b) < arr[1, b[1]]
        """
        expect = """Program([VarDecl(Id(x), None, var, ArrayCell(CallExpr(Id(func1), [Id(a), BinaryOp(..., ArrayCell(Id(arr), [NumLit(2.0), NumLit(3.0)]), StringLit(hello))]), [NumLit(1.0)])), VarDecl(Id(y), None, var, BinaryOp(<, BinaryOp(and, BinaryOp(+, BinaryOp(..., Id(str1), Id(str2)), Id(b)), BinaryOp(>=, Id(a), Id(b))), ArrayCell(Id(arr), [NumLit(1.0), ArrayCell(Id(b), [NumLit(1.0)])])))])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """var a <- arr[1]
        """
        expect = """Program([VarDecl(Id(a), None, var, ArrayCell(Id(arr), [NumLit(1.0)]))])"""
        self.assertTrue(TestAST.test(input, expect, 358)) 
        
    def test_59(self):
        input = """number arr[5] <- a
        """
        expect = """Program([VarDecl(Id(arr), ArrayType([5.0], NumberType), None, Id(a))])"""
        self.assertTrue(TestAST.test(input, expect, 359)) 
        
    def test_60(self):
        input = """number arr[5] <- getArr()
        """
        expect = """Program([VarDecl(Id(arr), ArrayType([5.0], NumberType), None, CallExpr(Id(getArr), []))])"""
        self.assertTrue(TestAST.test(input, expect, 360)) 
        
    def test_61(self):
        input = """
        ## This is comment
        func main()
            ## This is comment
            begin
            aPI <- 3.14
            end
            ## This is comment
        ## This is comment
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(aPI), NumLit(3.14))]))])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    
    def test_62(self):    
        input = """
        func main() begin ## This is comment
        end
        func main() 
            begin 
                ## This is comment
            end
        func main()
            ## comment1
            begin
                ## comment2
                ## comment3
                number a <- 1 + 2 + fun()
                number arr[1] <- 1
                ## comment4
            end
            ## This is comment
        """
        expect = """Program([FuncDecl(Id(main), [], Block([])), FuncDecl(Id(main), [], Block([])), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(2.0)), CallExpr(Id(fun), []))), VarDecl(Id(arr), ArrayType([1.0], NumberType), None, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 362)) 
    
    def test_63(self):    
        input = """
        func main()
            begin
            number a <- 2 + 1 / 3
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(2.0), BinaryOp(/, NumLit(1.0), NumLit(3.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    
    def test_64(self):    
        input = """
        func main()
            begin
            a(2)
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(a), [NumLit(2.0)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test_65(self):    
        input = """
        func main()
            begin
            a[1]<- 2
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 365))
                
    def test_66(self): 
        input = """
        number a
        func main()
            begin   
                if(true) a <- 1
                ## This is comment
                
                if(true) 
                    ## This is comment
                    a <- 1
                    ## This is comment
                else a <- 2
                ## This is comment
                
                if (1) a <- 1
                elif (1 < 2)
                    ## This is comment
                    
                    a <- 2
                    ## This is comment
                elif (1 > 2) a <- 3
                
                if (1) a<- 1
                elif (1 ... 2) a <- 1
                elif (2) a <- 1
                else a <- 3   
            end
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None), FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(a), NumLit(1.0))), [], None), If((BooleanLit(True), AssignStmt(Id(a), NumLit(1.0))), [], AssignStmt(Id(a), NumLit(2.0))), If((NumLit(1.0), AssignStmt(Id(a), NumLit(1.0))), [(BinaryOp(<, NumLit(1.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(>, NumLit(1.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(3.0)))], None), If((NumLit(1.0), AssignStmt(Id(a), NumLit(1.0))), [(BinaryOp(..., NumLit(1.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), (NumLit(2.0), AssignStmt(Id(a), NumLit(1.0)))], AssignStmt(Id(a), NumLit(3.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 366))  
    
    def test_67(self):    
        input = """
        func main()
            begin   
                if (a < 1)
                    a <- a + 1
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(1.0)), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 367))        
        
    def test_68(self): 
        input = """
        number a
        func main()
            begin
            for i until i >= 10 by 1
                ## This is comment
                
                a <- a + 1
            ## This is comment
            end
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None), FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 368))    
    
    def test_69(self):    
        input = """
        number a
        func main()
            begin
            for i until i >= 10 by 1
                a <- a + 1
            end
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None), FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 369))    

    def test_70(self):
        input = """
        number a
        func main()
            begin
            for i until i <= 10 by 1
                a <- a + 1
            end
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None), FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 370)) 
    
    def test_71(self):    
        input = """
        func main()
        begin 
            for i until i >= 10 by (1+3)/2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), BinaryOp(/, BinaryOp(+, NumLit(1.0), NumLit(3.0)), NumLit(2.0)), Block([Break, Continue])), For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [NumLit(1.0)])), For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [NumLit(1.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 371))  
    
    def test_72(self):    
        input = """
        func main()
            begin
            for i until i >= 10 by 1
                i <- i + 1
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 372)) 
        
    def test_73(self): 
        input = """
        func main()
            return 1 + 1
        """    
        expect = """Program([FuncDecl(Id(main), [], Return(BinaryOp(+, NumLit(1.0), NumLit(1.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """
        func main()
            begin
            readBool()
            end
        """    
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(readBool), [])]))])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    
    def test_75(self):    
        input = """
        func main()
        begin 
            return 1
            return main()
            main(1,2)
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([Return(NumLit(1.0)), Return(CallExpr(Id(main), [])), CallStmt(Id(main), [NumLit(1.0), NumLit(2.0)]), CallStmt(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0)), Id(a), BinaryOp(..., Id(c), Id(e))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 375))  
     
    def test_76(self):   
        input = """
        func main()
            return 1 + 2
        """
        expect = """Program([FuncDecl(Id(main), [], Return(BinaryOp(+, NumLit(1.0), NumLit(2.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 376))      
    
    def test_77(self):    
        input = """
        func main()
            return a
        """
        expect = """Program([FuncDecl(Id(main), [], Return(Id(a)))])"""
        self.assertTrue(TestAST.test(input, expect, 377)) 

    def test_78(self):    
        input = """
        func main()
            return arr[1]
        """
        expect = """Program([FuncDecl(Id(main), [], Return(ArrayCell(Id(arr), [NumLit(1.0)])))])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_79(self):    
        input = """
        func main()
            return arr[1,2]
        """
        expect = """Program([FuncDecl(Id(main), [], Return(ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0)])))])"""
        self.assertTrue(TestAST.test(input, expect, 379))
                
    def test_80(self):
        input = """
        number x
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    return false
                end
                begin
                end
                return true
            end
        """    
        expect = """Program([VarDecl(Id(x), NumberType, None, None), FuncDecl(Id(main), [], Block([Block([Block([AssignStmt(Id(x), NumLit(1.0))]), Block([Return(BooleanLit(True))]), Return(BooleanLit(False))]), Block([]), Return(BooleanLit(True))]))])"""
        self.assertTrue(TestAST.test(input, expect, 380))
     
    def test_81(self):
        input = """var a <- 2
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(2.0))])"""
        self.assertTrue(TestAST.test(input, expect, 381))        

    def test_82(self):
        input = """
        func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 382))   
        
    def test_83(self):    
        input = """
            func isPrime(number x)
            
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
            func isPrime(number x)
            begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
            return true
            end
        """
        expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
        self.assertTrue(TestAST.test(input, expect, 383))  

    def test_84(self):
        input = """
        func a() return 1 ## This is comment
        """
        expect = """Program([FuncDecl(Id(a), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 384))   
    
    def test_85(self):    
        input = """
            number x <- x 
            number x <- y
        """
        expect = """Program([VarDecl(Id(x), NumberType, None, Id(x)), VarDecl(Id(x), NumberType, None, Id(y))])"""
        self.assertTrue(TestAST.test(input, expect, 385)) 
    
    def test_86(self):    
        input = """
        func a()
        begin
        end
        
        func b()
        begin

            number x <- 1
            
        end
        
        func c()
        begin 
        end
        func d() begin 
        end
        func e() begin 
        end
        func f() begin ## This is comment
        end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([])), FuncDecl(Id(b), [], Block([VarDecl(Id(x), NumberType, None, NumLit(1.0))])), FuncDecl(Id(c), [], Block([])), FuncDecl(Id(d), [], Block([])), FuncDecl(Id(e), [], Block([])), FuncDecl(Id(f), [], Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 386))  
        
    def test_87(self):
        input = """    
        func a()
        begin
            break
        end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([Break]))])"""
        self.assertTrue(TestAST.test(input, expect, 387)) 
   
    def test_88(self):     
        input = """    
        func a()
        begin
            break
            return 1
        end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([Break, Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 388))   
    
    def test_89(self):    
        input = """    
        func a()
        begin
            if (x <= 1) return false
            if (x <= 1 )
                return false 
        end ## This is comment
        """
        expect = """Program([FuncDecl(Id(a), [], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 389))  
    
    def test_90(self):    
        input = """    
        func a()
            return x
        """
        expect = """Program([FuncDecl(Id(a), [], Return(Id(x)))])"""
        self.assertTrue(TestAST.test(input, expect, 390))  
    
    def test_91(self):    
        input = """    
        func a()
        begin
            if (x <= 1) return false
        end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 391))  
    
    def test_92(self):    
        input = """    
        func a()
        begin
            number arr[1,2] <- 5
        end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([VarDecl(Id(arr), ArrayType([1.0, 2.0], NumberType), None, NumLit(5.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 392))  
    
    def test_93(self):    
        input = """    
        func a()
            return 
        var a <- 1
        """
        expect = """Program([FuncDecl(Id(a), [], Return()), VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 393))  
        
    def test_94(self):
        input = """    
        func a(number a[1,1])
        """
        expect = """Program([FuncDecl(Id(a), [VarDecl(Id(a), ArrayType([1.0, 1.0], NumberType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 394))  
    
    def test_95(self):    
        input = """    
            var a <- a[1]
        """
        expect = """Program([VarDecl(Id(a), None, var, ArrayCell(Id(a), [NumLit(1.0)]))])"""
        self.assertTrue(TestAST.test(input, expect, 395))  
    
    def test_96(self):    
        input = """    
            number a[1] <- 1
        """
        expect = """Program([VarDecl(Id(a), ArrayType([1.0], NumberType), None, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input, expect, 396))  
    
    def test_97(self):    
        input = """    
        func a()
            begin
                a[1] <- 1
            end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 397)) 
        
    def test_98(self):     
        input = """    
            var a <- [1,2,3]
        """
        expect = """Program([VarDecl(Id(a), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 398)) 
        
    def test_99(self): 
        input = """    
            string a[1,2]
        """
        expect = """Program([VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 399)) 
    
    def test_100(self):    
        input = """    
        func a()
            begin 
                number a <- 1
            end
        """
        expect = """Program([FuncDecl(Id(a), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 400)) 