
from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    
    # program: (NEWLINE)* list_declared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # list_declared:  declared list_declared |  declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]


    # declared: function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.variables())


    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()


    # variables: keyword_var | implicit_var | implicit_dynamic;
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        elif ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        return self.visit(ctx.implicit_dynamic())


    # keyword_var: typ IDENTIFIER (OPEN_BRACKET list_number_lit CLOSE_BRACKET)? (ASSIGN expression)?;
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        if ctx.list_number_lit():
            if ctx.expression():
                return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.list_number_lit()), self.visit(ctx.typ())), None, self.visit(ctx.expression()))
            return VarDecl(name = Id(ctx.IDENTIFIER().getText()), varType = ArrayType(self.visit(ctx.list_number_lit()), self.visit(ctx.typ())))
        if ctx.expression():
            return VarDecl(name = Id(ctx.IDENTIFIER().getText()), varType = self.visit(ctx.typ()), varInit = self.visit(ctx.expression()))
        return VarDecl(name = Id(ctx.IDENTIFIER().getText()), varType = self.visit(ctx.typ()))


    # list_number_lit: NUM_LIT COMMA list_number_lit | NUM_LIT;
    def visitList_number_lit(self, ctx:ZCodeParser.List_number_litContext):
        if ctx.list_number_lit():
            return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.list_number_lit())
        return [float(ctx.NUM_LIT().getText())]


    # implicit_var: VAR IDENTIFIER ASSIGN expression;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, 'var', self.visit(ctx.expression()))


    # implicit_dynamic: DYNAMIC IDENTIFIER (ASSIGN expression)?;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.expression():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, 'dynamic', self.visit(ctx.expression()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, 'dynamic', None)


    # function: FUNC IDENTIFIER OPEN_PAREN param_list? CLOSE_PAREN (ignore? return_statement | ignore? block_statement | ignore);
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        if ctx.param_list():
            if ctx.return_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_list()), self.visit(ctx.return_statement()))
            elif ctx.block_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_list()), self.visit(ctx.block_statement()))
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_list()))
        else:
            if ctx.return_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), [], body = self.visit(ctx.return_statement()))
            elif ctx.block_statement():
                return FuncDecl(Id(ctx.IDENTIFIER().getText()), [], body = self.visit(ctx.block_statement()))
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), [])


    # param_list: param_declaration COMMA param_list | param_declaration;
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        if ctx.param_list():
            return [self.visit(ctx.param_declaration())] + self.visit(ctx.param_list())
        return [self.visit(ctx.param_declaration())]


    # param_declaration: typ IDENTIFIER (OPEN_BRACKET list_number_lit CLOSE_BRACKET)?;
    def visitParam_declaration(self, ctx:ZCodeParser.Param_declarationContext):
        if ctx.list_number_lit():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.list_number_lit()), self.visit(ctx.typ())))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()))


    # index_operator: expression | expression COMMA index_operator;
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        if ctx.index_operator():
            return [self.visit(ctx.expression())] + self.visit(ctx.index_operator())
        return [self.visit(ctx.expression())]
    

    # statement: declaration_statement | assignment_statement | if_statement | for_statement | break_statement
	#		| continue_statement | return_statement  | call_statement | block_statement;
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        if ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.for_statement():
            return self.visit(ctx.for_statement())
        if ctx.break_statement():
            return self.visit(ctx.break_statement())
        if ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        if ctx.return_statement():
            return self.visit(ctx.return_statement())
        if ctx.call_statement():
            return self.visit(ctx.call_statement())
        if ctx.block_statement():
            return self.visit(ctx.block_statement())



    # declaration_statement: variables ignore;
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.variables())


    # assignment_statement: IDENTIFIER (OPEN_BRACKET expression_list CLOSE_BRACKET)? ASSIGN expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        if ctx.expression_list():
            return Assign(ArrayCell(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expression_list())), self.visit(ctx.expression()))
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression()))


    # if_statement: IF OPEN_PAREN expression CLOSE_PAREN ignore? statement elif_list (ELSE ignore? statement)?;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.expression()),self.visit(ctx.statement()[0]),self.visit(ctx.elif_list()), None)
        return If(self.visit(ctx.expression()),self.visit(ctx.statement()[0]),self.visit(ctx.elif_list()), self.visit(ctx.statement()[1]))


    # elif_list: ELIF OPEN_PAREN expression CLOSE_PAREN ignore? statement elif_list | ;
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [(self.visit(ctx.expression()), self.visit(ctx.statement()))] + self.visit(ctx.elif_list())


    # for_statement: FOR IDENTIFIER UNTIL expression BY expression ignore? statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression()[0]), self.visit(ctx.expression()[1]), self.visit(ctx.statement()))


    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()


    # return_statement: RETURN expression? ignore;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()


    # call_statement: IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        if ctx.expression_list():
            return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression_list()))
        return CallStmt(Id(ctx.IDENTIFIER().getText()), [])


    # block_statement: BEGIN ignore block_list? END ignore;.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        if ctx.block_list():
            return Block(self.visit(ctx.block_list()))
        return Block([])


    # block_list: statement block_list | statement;
    def visitBlock_list(self, ctx:ZCodeParser.Block_listContext):
        if ctx.block_list():
            return [self.visit(ctx.statement())] + self.visit(ctx.block_list())
        return [self.visit(ctx.statement())]

    # expression: expression1 CONCAT expression1 | expression1;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            operator = ctx.CONCAT().getText()
            left = self.visit(ctx.expression1()[0])
            right = self.visit(ctx.expression1()[1])
            return BinaryOp(operator, left, right)
        return self.visit(ctx.expression1()[0])


    # expression1: expression2 (EQUAL | EQUAL_STRING | NOT_EQUAL | SMALLER | GREATER | SMALLER_EQUAL | GREATER_EQUAL) expression2 | expression2;
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 3:
            if ctx.EQUAL():
                operator = ctx.EQUAL().getText()
            elif ctx.EQUAL_STRING():
                operator = ctx.EQUAL_STRING().getText()
            elif ctx.NOT_EQUAL():
                operator = ctx.NOT_EQUAL().getText()
            elif ctx.SMALLER():
                operator = ctx.SMALLER().getText()
            elif ctx.GREATER():
                operator = ctx.GREATER().getText()
            elif ctx.SMALLER_EQUAL():
                operator = ctx.SMALLER_EQUAL().getText()
            elif ctx.GREATER_EQUAL():
                operator = ctx.GREATER_EQUAL().getText()
            left = self.visit(ctx.expression2()[0])
            right = self.visit(ctx.expression2()[1])
            return BinaryOp(operator, left, right)
        return self.visit(ctx.expression2()[0])


    # expression2: expression2 (AND_OP | OR_OP) expression3 | expression3;
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 3:
            if ctx.AND_OP():
                operator = ctx.AND_OP().getText()
            elif ctx.OR_OP():
                operator = ctx.OR_OP().getText()
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(operator, left, right)
        return self.visit(ctx.expression3())


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                operator = ctx.ADD().getText()
            elif ctx.SUB():
                operator = ctx.SUB().getText()
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            return BinaryOp(operator, left, right)
        return self.visit(ctx.expression4())


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 3:
            if ctx.MUL():
                operator = ctx.MUL().getText()
            elif ctx.DIV():
                operator = ctx.DIV().getText()
            elif ctx.MOD():
                operator = ctx.MOD().getText()
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(operator, left, right)
        return self.visit(ctx.expression5())


    # expression5: NOT_OP expression5 | expression6;
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 2:
            operator = ctx.NOT_OP().getText()
            operand = self.visit(ctx.expression5())
            return UnaryOp(operator, operand)
        return self.visit(ctx.expression6())


    # expression6: (ADD | SUB) expression6 | expression7;
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 2:
            if  ctx.ADD():
                operator = ctx.ADD().getText()
            elif ctx.SUB():
                operator = ctx.SUB().getText()
            operand = self.visit(ctx.expression6())
            return UnaryOp(operator, operand)
        return self.visit(ctx.expression7())


    # expression7: (IDENTIFIER | IDENTIFIER OPEN_PAREN index_operator? CLOSE_PAREN) OPEN_BRACKET index_operator CLOSE_BRACKET | expression8;
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.index_operator()[0]))
        elif len(ctx.index_operator()) == 2:
            return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.index_operator()[0])), self.visit(ctx.index_operator()[1]))
        return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), []), self.visit(ctx.index_operator()[0]))


    # expression8:  literals | IDENTIFIER | IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN | OPEN_PAREN expression CLOSE_PAREN;
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        if ctx.getChildCount() == 1:
            if ctx.IDENTIFIER():
                return Id(ctx.IDENTIFIER().getText())
            elif ctx.literals():
                return self.visit(ctx.literals())
        elif ctx.IDENTIFIER():
            if ctx.expression_list():
                return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expression_list()))
            return CallExpr(Id(ctx.IDENTIFIER().getText()), [])
        return self.visit(ctx.expression())


    # literals: NUM_LIT | STRING_LIT | TRUE | FALSE | array_lit ;
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())

    # array_lit: OPEN_BRACKET expression_list CLOSE_BRACKET;
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.expression_list()))


    # expression_list: expression COMMA expression_list | expression;
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        if ctx.expression_list():
            return [self.visit(ctx.expression())] + self.visit(ctx.expression_list())
        return [self.visit(ctx.expression())]


    # ignore: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None