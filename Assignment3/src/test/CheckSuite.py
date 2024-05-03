import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test401(self):
        input = """
            func f()
            begin
                dynamic x
                x <- [[1, 2, 3], [4, 5, 6]]
                return x[0, 0]
            end

            func main()
            begin
                number x <- f()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test402(self):
        input = """
            func f(number x)

            func main()
            begin
                number x <- f(2)
                writeNumber(x)
            end

            func f(number x)   
            begin
                if (x >= 2) return f(x - 1) + f(x - 2)
                return 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test403(self):
        input = """
            func main() 
            begin
                dynamic x
                number a[3, 1, 2] <- [[[[x]]], [[x,x]], [[x]]]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0, 1.0, 2.0], NumberType), None, ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x)))), ArrayLit(ArrayLit(Id(x), Id(x))), ArrayLit(ArrayLit(Id(x)))))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test404(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test405(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a <- 1 + [[[[x]]]]
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x)))))))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test406(self):
        input = """
            dynamic x <- f(2)
            func f(number x)

            func main()
            begin

            end
        """
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test407(self):
        input = """
            func f(number x)

            dynamic x <- f(2) + 1

            func f(number y)
            begin
                if (y <= 1) return 1
                return y * f(y - 1)
            end

            func main()
            begin
                return 2
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test408(self):
        input = """
            func f(number x)

            dynamic x <- f(2) + 1

            func main()
            begin
                return
            end
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test409(self):
        input = """
            func f(number x[2, 3])
                return x[2]

            func main()
            begin
                number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                writeNumber(f()[2])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test410(self):
        input = """
            func f(number x[2, 3])
                return x

            func main()
            begin
                number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                writeNumber(f(x)[0, 1])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test411(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test412(self):
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test413(self):
        input = """
            func main() begin
                dynamic x
                number a[3, 2] <- [[x], [x], [x]]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x)), ArrayLit(Id(x)), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test414(self):
        input = """
            dynamic x
            number a[2] <- [[x],[x,x]]
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0], NumberType), None, ArrayLit(ArrayLit(Id(x)), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test415(self):
        input = """
            func foo(number a, string a)
            func foo(number a, string a) return 
            func main() return
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test416(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                number b
                if (true) number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test417(self):
        input = """
            func findMax(number x[10], number n)
            begin
                if (n = 1) return x[0]
                number k <- findMax(x, n - 1)
                if (k >= x[n]) return k
                return x[n]
            end

            func main()
            begin
                dynamic x <- [3, 4, 0, 1, 2, 7, 9, 8, 5, 6]
                writeNumber(findMax(x, 10))
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test418(self):
        input = """
            func main()
            begin
                number x <- 2 + true
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test419(self):
        input = """
            func main() 
            begin
                dynamic x
                if ([x]) x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(x)), AssignStmt(Id(x), NumLit(1.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test420(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                number x[3, 3] <- [a, b, c]
                a <- [1, 2, 3]
                b <- [4, 5, 6]
                c <- [7, 8, 9]
                writeNumber(a[0] + b[0] + c[0])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test421(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until y[1] by 1
                    return
            end
        """
        expect = "Type Cannot Be Inferred: For(Id(x), ArrayCell(Id(y), [NumLit(1.0)]), NumLit(1.0), Return())"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test422(self):
        input = """
            func f(number x[2, 3])
    
            func main()
            begin
                dynamic a
                number x[2, 3] <- f(a)
                a[0] <- [1, 2, 3]
            end

            func f(number x[2, 3])
                return x
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test423(self):
        input = """
            func main() 
            begin
                dynamic x
                return x[1]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayCell(Id(x), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test424(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                number a <- 1 + foo([[x]])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(x)))])))"
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test425(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test426(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a[1,1,1,1] <- [[[[x]]]]
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test427(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test428(self):
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test429(self):
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test430(self):
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test431(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test432(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    number i
                end
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test433(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                number x[2, 2] <- [a, [b, 2]]
                a <- 2
                b <- 3
                c <- true
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test434(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                number x[3, 2] <- [a, b, [c, 0]]
                a <- [1]
                b <- [3, 4]
                c <- 0
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test435(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                dynamic x <- [readNumber(), a, b, c]
                a <- 3
                b <- x[0]
                c <- a + b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test436(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    begin
                        number i
                    end
                end
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test437(self):
        input = """
            func main()
            begin
                dynamic x
                if (x) writeString("x is infer to true value")
                else writeString("x is infer to false value")
                x <- 1 + true
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test438(self):
        input = """
            func main()
            begin
                dynamic x
                if (x) writeString("x is infer to true value")
                else writeString("x is infer to false value")
                x <- not (true and not false) and not (false and not true)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test439(self):
        input = """
            func a(number c)
            
            func a() begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test440(self):
        input = """
            func f()
            begin
                dynamic x
                x <- (x - 2) * (x + true)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test441(self):
        input = """
            number a <- 1 + "Hello"
            func main()
            return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test442(self):
        input = """
        func f()

        func main()
        begin
            number x <- g(1, 2, 3)
        end
        """
        expect = "Undeclared Function: g"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test443(self):
        input = """
            number x
            number y
            func f()

            func main()
                return
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test444(self):
        input = """
            func main() begin 
                number a[1,2,3,4]
                var c <- a[1]
                number b[2,3,4]
                c <- b
                 number d[1,3,4]
                 c <- d
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test445(self):
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test446(self):
        input = """
            func f(number x)
            begin
                return f(x)
            end

            func main()
            begin
                dynamic d <- f(10)
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test447(self):
        input = """
            func f(number x)
            begin
                return 1
            end

            func main()
            begin
                 f(2024)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2024.0)])"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test448(self):
        input = """
            func main()
            begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test449(self):
        input = """
            func main()
            begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test450(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test451(self):
        input = """
            func add(number x, number y)

            func main()
            begin
                number x <- readNumber()
                number y <- readNumber()
                dynamic a <- add(x, y) + 1
            end

            func add(number x, number y)
                return "Hello"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test452(self):
        input = """
            func add(number x, number y)

            func main()
            begin
                dynamic a
                a[0] <- [1, 2, 3]
            end

            func add(number x, number y)
                return "Hello"
        """
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test453(self):
        input = """
            func main()
            begin
                number arr[3, 2] <- [[1, 2], [3, 4], [5, 6]]
                number b[2] <- arr[1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test454(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test455(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                number arr[2, 2] <- [[a, b]]
                number c[2, 2] <- arr
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test456(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                var arr <- [[a], [b], [c], [1]]
                arr <- [[1], [2], [3], [4]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test457(self):
        input = """
            func main()
            begin
                dynamic x <- "Hello"
                if (x == "Hello") writeString(x)
                else writeString("Something weird!")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test458(self):
        input = """
            func main()
            begin
                dynamic x <- [1, 2, 3]
                dynamic a <- x
                writeNumber(a[0])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test459(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test460(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test461(self):
        input = """
            func f(number a[3], number b[3])
                return

            func main()
            begin
                f([1, 3, 2], [1, "Hello", 2])
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test462(self):
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test463(self):
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test464(self):
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test465(self):
        input = """
            func f(number x[2, 3])
                return x[0]

            func main()
            begin
                dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test466(self):
        input = """
            func f(number n)

            func main()
            begin
                var i <- f(2, 3)
            end

            func f(number a)
                return a
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test467(self):
        input = """
            func f(number x, number y)

            func main()
            begin
                var i <- f(2)
            end

            func f(number a)
                return a
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test468(self):
        input = """
            dynamic a
            func main()
            begin
                var i <- a ... 2.75
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test469(self):
        input = """
            dynamic a
            func main()
            begin
                var i <- a[2] ... 2.75
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75)))"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test470(self):
        input = """
            func main()
            begin
                if (1) writeBool(true)
                else writeBool(false)
            end
        """
        expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test471(self):
        input = """
            func main()

            func main()

            func main()
            begin
                if (1) writeBool(true)
                else writeBool(false)
            end
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test472(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test473(self):
        input = """
            func main() begin 
                number i
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    break
                    continue
                    for i until true by 1
                    begin
                        for i until true by 1
                        begin
                            break
                            continue
                        end
                        break
                        continue
                    end
                        break
                        continue
                    begin
                        break
                        continue
                    end
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test474(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                var arr <- [[a, 1], [b, true], [c, "Hello"]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test475(self):
        input = """
            func a()
            
            func a(number c) begin 
            end
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test476(self):
        input = """
            func main()
            begin
                var x <- [10, 20, 40]
                var y <- [true, false, true]
                number a[2, 3] <- [x, y]
                writeNumber(a[0, 0])
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test477(self):
        input = """
            func a(number a) begin 
            end
            func a(string c)
            func main() begin 
            end
        """
        expect = "Redeclared Function: a"

        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test478(self):
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(string a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test479(self):
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number writeString
                number c
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test480(self):
        input = """
            func main()
            begin
                var x <- [[1, 2], [3, 4, 5]]
                writeNumber(x[0, 2])
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test481(self):
        input = """
            func test(number x)
            begin
                var y <- test
                test(2024)
            end
        """
        expect = "Undeclared Identifier: test"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test482(self):
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                string e
            end
        """
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test483(self):
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number e
                    number z
                    begin
                        number e
                    end
                    number z
                end
            end
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test484(self):
        input = """
            dynamic a
            func main()
            begin
                var x <- [a, [1, 2, 3]]
                a <- [1, 9, 6]
                x <- [[3, 9, 6], [1, 3, 2]]
                writeNumber(x[0, 0])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test485(self):
        input = """
            func a(number a, number c[3])
            func main() begin 
            end
            func a(number a, number c[3]) begin
                number e
                begin
                    number a
                    number e
                    number k
                    string k
                end
            end
        """
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test486(self):
        input = """
            func a(number a[1,3,2])
            func main() begin 
            end
            func a(string a[1,3,2]) begin
            end
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test487(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c <- a ... ", world!"
                a <- b
                b <- [1, 2, 3]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test488(self):
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- a()
                var d <- b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test489(self):
        input = """
            func a()
                return 1
            func main(number k, number j) begin 
                var c <- k()
            end
        """
        expect = "Undeclared Function: k"
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test490(self):
        input = """
            dynamic x
            func f(number x)
                return x + 1

            func main()
            begin
                x <- f(20, 30, 40) + 1
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(20.0), NumLit(30.0), NumLit(40.0)])"
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test491(self):
        input = """
            func main() begin 
                string i
                dynamic j
                
                if (true) return
                elif (true) return
                elif (i) return
                elif (false) return
                else return
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), Return()), [(BooleanLit(True), Return()), (Id(i), Return()), (BooleanLit(False), Return())], Return())"
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test492(self):
        input = """
            func main() begin 
                number i
                dynamic j
                
                if (true) return
                elif (false) return
                elif (j) return
                else return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test493(self):
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test494(self):
        input = """
        func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                dynamic x <- [a, b, c]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test495(self):
        input = """
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                dynamic x
                x <- [a, b, [c]]
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test496(self):
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test497(self):
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test498(self):
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test499(self):
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"

        self.assertTrue(TestChecker.test(input, expect, 499))
    
    def test500(self):
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 500))