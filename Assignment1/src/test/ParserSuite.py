import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))   
    
    def test_2(self):    
        input = """ 
            var a
        """
        expect = "Error on line 2 col 18: \n"
        self.assertTrue(TestParser.test(input, expect, 202))   
    
    def test_3(self):   
        input = """ 
            dynamic a[5] <- 3
        """
        expect = "Error on line 2 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 203))         

    def test_4(self):
        input = """ 
            bool a["hello"]
            bool b[[1,2]]
            bool c[1+1]
        """
        expect = "Error on line 2 col 19: hello"
        self.assertTrue(TestParser.test(input, expect, 204))   
    
    def test_5(self):    
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 205)) 

    def test_6(self):
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 206))  
        
    def test_7(self):
        input = """ 
            dynamic a[1]
        """
        expect = "Error on line 2 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 207))
        
    def test_8(self):
        input = """ 
            var a
            number b <- 5
        """
        expect = "Error on line 2 col 18: \n"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    def test_9(self):
        input = """ 
            var a <- 6
            number b 
            dynamic c
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209)) 
        
    def test_10(self):
        input = """ 
            var a <- 6
            number b <- 5
            dynamic c
            var d
        """
        expect = "Error on line 5 col 18: \n"
        self.assertTrue(TestParser.test(input, expect, 210)) 
        
    def test_11(self):
        input = """ 
            func main()
            func main(number a[2],bool b[1,2,3], bool c[1,2,3], string s, bool d)
            func main(number num1, number num2)
                var t <- 1
            func main(number y <- c)
        """
        expect = "Error on line 6 col 31: <-"
        self.assertTrue(TestParser.test(input, expect, 211))       
    
    def test_12(self):    
        input = """ 
            func main()
            ## This is comment
            func main() func main(dynamic a) ## This is comment
        """
        expect = "Error on line 4 col 24: func"
        self.assertTrue(TestParser.test(input, expect, 212))  

    def test_13(self):
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_14(self):    
        input = """ 
            func main(dynamic a)
        """
        expect = "Error on line 2 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 214))     
        
    def test_15(self):    
        input = """ 
            func main(number a, dynamic b)
        """
        expect = "Error on line 2 col 32: dynamic"
        self.assertTrue(TestParser.test(input, expect, 215))    
        
    def test_16(self):    
        input = """ 
            func main(number a, dynamic b)
        """
        expect = "Error on line 2 col 32: dynamic"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test_17(self):    
        input = """ 
            func main(number func()[2])
        """
        expect = "Error on line 2 col 29: func"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test_18(self):    
        input = """ 
            func main(number a <- 5)
        """
        expect = "Error on line 2 col 31: <-"
        self.assertTrue(TestParser.test(input, expect, 218))       
        
    def test_19(self):    
        input = """ 
            func main(number a , bool b, string s)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_20(self):    
        input = """ 
            func main(number a[5], number b)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))  
        
    def test_21(self):
        input = """ 
            ##This is comment
            ##This is comment
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 221))   
    
    def test_22(self):    
        input = """ 
            func main(string a) 
                begin 
                    break ## This is comment
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 222))    

    def test_23(self):
        input = """ 
            func main(number a[1,2,3]) ##This is comment
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 223))    
    
    def test_24(self):
        input = """ 
            ##This is comment
            ##This is comment
            
            func main(number a)
            begin
            var c <- 1 ##Declare variable
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))                  

    def test_26(self):
        input = """ 
            ## This is comment
            
            var a <- 1 ## This is comment
            ## This is comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))   
    
    def test_27(self):    
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 227))  

    def test_28(self):
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 228))  
        
    def test_29(self):
        input = """
            func main(number a) 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229)) 
        
    def test_30(self):
        input = """var a <- 1 ## This is comment"""
        expect = "Error on line 1 col 29: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 230)) 
    
    def test_31(self):
        input = """ var str <- "Hai" ... "Dang" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test_32(self):    
        input = """ var str <- "Ha" ... "i" ... "Dang" 
        """
        expect = "Error on line 1 col 25: ..."
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test_33(self):    
        input = """ 
            var a <- 4 > 5 
            var b <- 1 >= 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        
    def test_34(self):
        input = """
            var a <- 4 >= 5
            var b <- 1 >= 2 < 3
        """
        expect = "Error on line 3 col 28: <"
        self.assertTrue(TestParser.test(input, expect, 234))
        
        
    def test_35(self):
        input = """ var a <- true > x >= z 
        """
        expect = "Error on line 1 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 235))
        
        
    def test_36(self):
        input = """
            func findMax(number a, number b)
            begin
            if (0 < a < b)
                return b
            else
                return a
        """
        expect = "Error on line 4 col 22: <"
        self.assertTrue(TestParser.test(input, expect, 236))
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))  
        
    def test_38(self):
        input = """
            func concatString(string a, string b, string c)
                return (a ... b ... c)
        """
        expect = "Error on line 3 col 32: ..."
        self.assertTrue(TestParser.test(input, expect, 238)) 
        
    def test_39(self):
        input = """
            func concatString(string a, string b)
                return (a ... b)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239)) 
              
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240)) 

    def test_41(self):
        input = """ 
            var a <- 1 + 2
            number b <- 1 + 2 + 3 -4 + 5
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        
    def test_42(self):
        input = """ 
            number a <- 1 * 2 / 3 + 4 - 7
            number b <- 2 + 1 * 8 - 14 / 3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
        
    def test_43(self):
        input = """ 
            var a <- x and y or z
            var b <- x or y or z
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
    def test_44(self):
        input = """ 
            var a <- x and y and z
            var b <- x == y or y < z
        """
        expect = "Error on line 3 col 33: <"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_45(self):            
        input = """var a <- 2 >= 1 and 1 > 2
        """
        expect = "Error on line 1 col 22: >"
        self.assertTrue(TestParser.test(input, expect, 245)) 
        
    def test_46(self):  
        input = """ 
            var a <- -1 + 2
            var b <- not not not a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246)) 
    
    def test_47(self):
        input = """var a <- - not 1
        """
        expect = "Error on line 1 col 11: not"
        self.assertTrue(TestParser.test(input, expect, 247)) 

    def test_48(self):
        input = """var VoTien <- - (not 1)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248)) 
        
    def test_49(self):
        input = """var a <- not not not not - - - - 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249)) 
        
    def test_50(self):
        input = """var a <- - - - - not not not not 1
        """
        expect = "Error on line 1 col 17: not"
        self.assertTrue(TestParser.test(input, expect, 250)) 
        
    def test_51(self):
        input = """ var a <- arr[1] + 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_52(self):    
        input = """var a <- arr[1,2] + b[[1],[1]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252)) 

    def test_53(self):    
        input = """var a <- arr[1,2] + getArr()[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        
    def test_54(self):    
        input = """var a <- arr[1,2][2,3] + b[[1],[1]]
        """
        expect = "Error on line 1 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 254))
        
    def test_55(self):
        input = """ 
            var a <- func1()
            var b <- func2(1,2)
            var c <- func3(x,array[1])[2]
            var d <- func4(x,str[3] ... "hi")[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))    

    def test_56(self):
        input = """ 
            var x <- func1() + -1 / 2 * 3 < 4 ... "string" > "hi"
            number arr[5] <-  [1, 2, 3, 4, 5] + [[1, 2 + 5 * 2 / 1, 2], [4, 5, 6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))  
        
    def test_57(self):
        input = """ 
            var x <- func1(a,arr[2,3] ... "hello")[1]
            var y <- (str1 ... str2) + b and (a >= b) < arr[1, b[1]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input = """var a <- arr[1]()
        """
        expect = "Error on line 1 col 15: ("
        self.assertTrue(TestParser.test(input, expect, 258)) 
        
    def test_59(self):
        input = """var arr[5] <- a
        """
        expect = "Error on line 1 col 7: ["
        self.assertTrue(TestParser.test(input, expect, 259)) 
        
    def test_60(self):
        input = """number arr[5] <- getArr()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260)) 
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
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
                number arr[1+a] <- 1
                ## comment4
            end
            ## This is comment
        """
        expect = "Error on line 14 col 28: +"
        self.assertTrue(TestParser.test(input, expect, 262)) 
    
    def test_63(self):    
        input = """
        func main()
            begin
            a + 1 <- 2
            end
        """
        expect = "Error on line 4 col 14: +"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_64(self):    
        input = """
        func main()
            begin
            a()<- 2
            end
        """
        expect = "Error on line 4 col 15: <-"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def test_65(self):    
        input = """
        func main()
            begin
            (a)[1]<- 2
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 265))
                
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))  
    
    def test_67(self):    
        input = """
        func main()
            begin   
                if (a <- 1)
            end
        """
        expect = "Error on line 4 col 22: <-"
        self.assertTrue(TestParser.test(input, expect, 267))        
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))    
    
    def test_69(self):    
        input = """
        number a
        func main()
            begin
            for i[1] until i >= 10 by 1
                a <- a + 1
            end
        """
        expect = "Error on line 5 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 269))    

    def test_70(self):
        input = """
        number a
        func main()
            begin
            for i+1 until i >= 10 by 1
                a <- a + 1
            end
        """
        expect = "Error on line 5 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 270)) 
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))  
    
    def test_72(self):    
        input = """
        func main()
            begin
            for i until i >= 10 by 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 272)) 
        
    def test_73(self): 
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """
        func main()
            begin
            readBool()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))  
     
    def test_76(self):   
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 276))      
    
    def test_77(self):    
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 277)) 

    def test_78(self):    
        input = """
        func main()
            return continue
        """
        expect = "Error on line 3 col 19: continue"
        self.assertTrue(TestParser.test(input, expect, 278))
        
    def test_79(self):    
        input = """
        func main()
            return func1()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
                
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
     
    def test_81(self):
        input = """var a <- 2"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 281))        

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))   
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))  

    def test_84(self):
        input = """
        func a() return 1 ## This is comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))   
    
    def test_85(self):    
        input = """
            number x <- x number x <- y
        """
        expect = "Error on line 2 col 26: number"
        self.assertTrue(TestParser.test(input, expect, 285)) 
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))  
        
    def test_87(self):
        input = """    
        func a()
        begin
            break continue
        end
        """
        expect = "Error on line 4 col 18: continue"
        self.assertTrue(TestParser.test(input, expect, 287)) 
   
    def test_88(self):     
        input = """    
        func a()
        begin
            return 1 break
        end
        """
        expect = "Error on line 4 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 288))   
    
    def test_89(self):    
        input = """    
        func a()
        begin
            if (x <= 1) return false
            if (x <= 1 )
                return false 
        end ## This is comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))  
    
    def test_90(self):    
        input = """    
        func a()
            fun()
        """
        expect = "Error on line 3 col 12: fun"
        self.assertTrue(TestParser.test(input, expect, 290))  
    
    def test_91(self):    
        input = """    
        func a()
            if x <= 1 return false
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 291))  
    
    def test_92(self):    
        input = """    
        func a()
            return if x <= 1 return false
        """
        expect = "Error on line 3 col 19: if"
        self.assertTrue(TestParser.test(input, expect, 292))  
    
    def test_93(self):    
        input = """    
        func a()
            return 
        var a <- []
        """
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 293))  
        
    def test_94(self):
        input = """    
        func a(number a[1+1])
        """
        expect = "Error on line 2 col 25: +"
        self.assertTrue(TestParser.test(input, expect, 294))  
    
    def test_95(self):    
        input = """    
            var a <- a[1][1]
        """
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 295))  
    
    def test_96(self):    
        input = """    
            var a <- 1[1]
        """
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.test(input, expect, 296))  
    
    def test_97(self):    
        input = """    
        func a()
            begin
                a[1][2] <- 1
            end
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 297)) 
        
    def test_98(self):     
        input = """    
            var a <- [1,2,3][1,2,3]
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 298)) 
        
    def test_99(self): 
        input = """    
            string a[1+1]
        """
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.test(input, expect, 299)) 
    
    def test_100(self):    
        input = """    
        func a()
            begin a <- 1
            end
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 300)) 