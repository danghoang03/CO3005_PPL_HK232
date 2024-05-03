from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    def __init__(self, eleType, ast):
        self.eleType = eleType
        self.ast = ast
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }
        
    def check(self):
        self.visit(self.ast, [{}])
        return None    
    
    def compareType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if len(LHS.size) == len(RHS.size):
                for size1, size2 in zip(LHS.size, RHS.size):
                    if size1 != size2:
                        return False
                if type(LHS.eleType) == type(RHS.eleType):
                    return True
            return False
        elif type(LHS) == type(RHS):
            return True
        return False
    
    def compareListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False
        for i in range(len(LHS)):
            if self.compareType(LHS[i], RHS[i]) == False:
                return False
        return True
                    
    def typeInfer_expr(self, LHS, RHS, ast, param):
        if type(LHS) is CannotBeInferredZcode or type(RHS) is CannotBeInferredZcode:
            return True
        elif type(LHS) in [VarZcode,FuncZcode] and type(RHS) in [VarZcode, FuncZcode]:
            return True
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) is ArrayZcode:
            return True
        elif type(LHS) is ArrayType and type(RHS) is ArrayZcode:
            RHS = self.visitArrayLiteral(RHS.ast, param, LHS)
            return self.typeInfer_expr(LHS, RHS, ast, param)
        elif type(RHS) is ArrayZcode:
            return True
        elif type(LHS) in [VarZcode, FuncZcode]:
            LHS.typ = RHS
        elif type(RHS) in [VarZcode, FuncZcode]:
            RHS.typ = LHS
        elif self.compareType(LHS, RHS) == False:
            raise TypeMismatchInExpression(ast)
        return False
        
    def typeInfer_stmt(self, LHS, RHS, ast, param):
        if type(LHS) is CannotBeInferredZcode or type(RHS) is CannotBeInferredZcode:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode,FuncZcode] and type(RHS) in [VarZcode, FuncZcode]:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) is ArrayType and type(RHS) is ArrayZcode:
            RHS = self.visitArrayLiteral(RHS.ast, param, LHS)
            self.typeInfer_stmt(LHS, RHS, ast, param)
        elif type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode, FuncZcode]:
            LHS.typ = RHS
        elif type(RHS) in [VarZcode, FuncZcode]:
            RHS.typ = LHS
        elif self.compareType(LHS, RHS) == False:
            raise TypeMismatchInStatement(ast)
        return False
            
    def visitProgram(self, ast: Program, param):
        for decl in ast.decl: 
            self.visit(decl, param)
        
        for key, val in self.listFunction.items():
            if val.body == False:
                raise NoDefinition(key)
            
        main = self.listFunction.get("main")
        if main is None:
            raise NoEntryPoint()
        if not(main.param == [] and isinstance(main.typ, VoidType)):
            raise NoEntryPoint()

        
    def visitVarDecl(self, ast: VarDecl, param):   
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        param[0][ast.name.name] = VarZcode(ast.varType)
        
        if ast.varInit:
            RHS = self.visit(ast.varInit, param)
            LHS = param[0].get(ast.name.name) if ast.varType is None else ast.varType
            cannotBeInferred = self.typeInfer_stmt(LHS, RHS , ast, param)
            
        return param

    def visitFuncDecl(self, ast: FuncDecl, param):
        if ast.name.name in self.listFunction:
            if ast.body is None and self.listFunction[ast.name.name].body == False:
                raise Redeclared(Function(), ast.name.name)
            elif self.listFunction[ast.name.name].body == True:
                raise Redeclared(Function(), ast.name.name)      
        
        if ast.body is None:
            typeParam = []
            for para in ast.param:
                typeParam += [para.varType]
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            return self.listFunction[ast.name.name]

        listParam = {}
        typeParam = []

        for para in ast.param:
            if para.name.name in listParam:
                raise Redeclared(Parameter(), para.name.name)
            listParam[para.name.name] = VarZcode(para.varType)
            typeParam += [para.varType]
        
        funcName = self.listFunction.get(ast.name.name) 
        
        if funcName:
            compareList = self.compareListType(typeParam, funcName.param)
            if compareList == False:
                raise Redeclared(Function(), ast.name.name)
            self.listFunction[ast.name.name].body = True
            self.function = self.listFunction[ast.name.name]

        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
        
        self.Return = False
        self.function = self.listFunction[ast.name.name]
        self.visit(ast.body, [listParam] + param)
        
        if self.Return == False:
            if self.listFunction[ast.name.name].typ is None:
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast: Id, param):
        flag = False
        for env in param:
            Id = env.get(ast.name)
            if Id is not None:
                if isinstance(Id, VarZcode):
                    flag = True
                    break
        if flag == False:
            raise Undeclared(Identifier(), ast.name)
        return Id.typ if Id.typ else Id

    def visitCallStmt(self, ast: CallStmt, param):
        method = self.listFunction.get(ast.name.name)
        
        if method is None:
            raise Undeclared(Function(), ast.name.name)

        listLHS = method.param
        listRHS = ast.args
        
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
    
        for i in range(len(listLHS)):
            LHS = method.param[i]
            RHS = self.visit(ast.args[i], param)
            cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)
            
        if method.typ is None: method.typ = VoidType()
        elif not self.compareType(method.typ, VoidType()): raise TypeMismatchInStatement(ast)
        return method.typ

    def visitCallExpr(self, ast: CallExpr, param):
        method = self.listFunction.get(ast.name.name)
        
        if method is None:
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = method.param
        listRHS = ast.args
        
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(listLHS)):
            LHS = method.param[i]
            RHS = self.visit(ast.args[i], param)
            cannotBeInferred = self.typeInfer_expr(LHS, RHS, ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            
        if method.typ is None: return method
        elif self.compareType(method.typ, VoidType()): raise TypeMismatchInExpression(ast)
        return method.typ

    def visitBlock(self, ast: Block, param):
        paramNew = [{}] + param
        for item in ast.stmt: 
            self.visit(item,paramNew) 

    def visitIf(self, ast:If, param):
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)   
            
        self.visit(ast.thenStmt, param)
        
        for elifBlock in ast.elifStmt:
            LHS = BoolType()
            RHS = self.visit(elifBlock[0], param)
            cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)  
            self.visit(elifBlock[1], param)
               
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

    def visitFor(self, ast: For, param):
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)  
        
        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)  
    
        LHS = NumberType()
        RHS = self.visit(ast.updExpr, param)
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)  
        
        self.BlockFor += 1 
        self.visit(ast.body, param)
        self.BlockFor -= 1 
        
    def visitContinue(self, ast: Continue, param):
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast: Break, param):
        if self.BlockFor == 0: raise MustInLoop(ast)
        
    def visitAssign(self, ast: Assign, param):
        RHS = self.visit(ast.rhs, param)
        LHS = self.visit(ast.lhs, param)
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param)                 
                

    def visitReturn(self, ast: Return, param):
        self.Return = True
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        LHS = self.function.typ if self.function.typ else self.function
        cannotBeInferred = self.typeInfer_stmt(LHS, RHS, ast, param) 
            
    def visitBinaryOp(self, ast: BinaryOp, param):
        op = ast.op    
        
        left = self.visit(ast.left, param)
        if op in ['+', '-', '*', '/', '%']:
            LHS = NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            LHS = NumberType() 
        elif op in ['and', 'or']:
            LHS = BoolType()
        elif op in ['==', '...']:
            LHS = StringType()
            
        cannotBeInferred = self.typeInfer_expr(LHS, left, ast, param)
        if cannotBeInferred: return CannotBeInferredZcode()

        right = self.visit(ast.right, param)
            
        cannotBeInferred = self.typeInfer_expr(LHS, right, ast, param)
        if cannotBeInferred: return CannotBeInferredZcode()
            
        if op in ['+', '-', '*', '/', '%']:
            return NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            return BoolType() 
        elif op in ['and', 'or']:
            return  BoolType()
        elif op in ['==']:
            return BoolType()
        elif op in ['...']:
            return StringType()

    def visitUnaryOp(self, ast: UnaryOp, param):    
        right = self.visit(ast.operand, param)
        op = ast.op
        if op in ['+','-']:
            LHS = NumberType()
            cannotBeInferred = self.typeInfer_expr(LHS, right, ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return NumberType()
            
        elif op in ['not']:
            LHS = BoolType()
            cannotBeInferred = self.typeInfer_expr(LHS, right, ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return BoolType()

    def visitArrayCell(self, ast: ArrayCell, param):
        arr = self.visit(ast.arr, param)
        if type(arr) in [BoolType, StringType, NumberType]:
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()
         
        for ele in ast.idx:
            LHS = NumberType()
            RHS = self.visit(ele, param)
            cannotBeInferred = self.typeInfer_expr(LHS, RHS, ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()

        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType) 

    def visitArrayLiteral(self, ast, param, typ = None):
        if typ is not None:
            result = typ
            typ = typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType) 
            
            
            for ele in ast.value:
                RHS = self.visit(ele, param)   
                if type(RHS) is CannotBeInferredZcode or type(typ) is CannotBeInferredZcode:
                    return CannotBeInferredZcode()
                if type(typ) is ArrayType and type(RHS) is ArrayZcode:
                    typ = self.visitArrayLiteral(RHS.ast, param, typ)
                elif type(RHS) is ArrayZcode:
                    return CannotBeInferredZcode()
                elif type(RHS) in [VarZcode, FuncZcode]:
                    RHS.typ = typ
            
            return self.visitArrayLiteral(ast, param)
        
        for ele in ast.value:
            checkTyp = self.visit(ele, param)
            if typ is None and type(checkTyp) in [BoolType, StringType, NumberType, ArrayType]:
                typ = checkTyp
            elif type(checkTyp) is CannotBeInferredZcode:
                return CannotBeInferredZcode()

        if typ is None:
            listType = []
            for ele in ast.value:
                listType += [self.visit(ele, param)]
            return ArrayZcode(listType, ast)
        
        for ele in ast.value:
            LHS = typ
            RHS = self.visit(ele, param)
            cannotBeInferred = self.typeInfer_expr(LHS, RHS, ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
                
           
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([float(len(ast.value))], typ)
        else:
            return ArrayType([float(len(ast.value))] + typ.size, typ.eleType)

    def visitNumberType(self, ast: NumberType, param): return NumberType()
    
    def visitBoolType(self, ast: BoolType, param): return BoolType()
    
    def visitStringType(self, ast :StringType, param): return StringType()
    
    def visitArrayType(self, ast: ArrayType, param): return ArrayType(ast.size, ast.eleType)
    
    def visitNumberLiteral(self, ast: NumberLiteral, param): return NumberType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, param): return BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, param): return StringType()
    

