// ID: 2110120
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

//program
program: (NEWLINE)* list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables ignore;

//4. Type
typ: NUMBER | BOOL | STRING;

//6.1 Variables
variables: keyword_var | implicit_var | implicit_dynamic;
keyword_var: typ IDENTIFIER (OPEN_BRACKET list_number_lit CLOSE_BRACKET)? (ASSIGN expression)?;
list_number_lit: NUM_LIT COMMA list_number_lit | NUM_LIT;
implicit_var: VAR IDENTIFIER ASSIGN expression;
implicit_dynamic: DYNAMIC IDENTIFIER (ASSIGN expression)?;

//6.2 Function
function: FUNC IDENTIFIER OPEN_PAREN param_list? CLOSE_PAREN (ignore? return_statement | ignore? block_statement | ignore);
param_list: param_declaration COMMA param_list | param_declaration;
param_declaration: typ IDENTIFIER (OPEN_BRACKET list_number_lit CLOSE_BRACKET)?;

//5.5 Index operators
index_operator: expression | expression COMMA index_operator;

//7. Statements
statement: declaration_statement | assignment_statement | if_statement | for_statement | break_statement
			| continue_statement | return_statement  | call_statement | block_statement;

//7.1. Variable declaration statement
declaration_statement: variables ignore;

//7.2 Assignment statement
assignment_statement: IDENTIFIER (OPEN_BRACKET expression_list CLOSE_BRACKET)? ASSIGN expression ignore;

//7.3 If statement
if_statement: IF OPEN_PAREN expression CLOSE_PAREN ignore? statement elif_list (ELSE ignore? statement)?;
elif_list: ELIF OPEN_PAREN expression CLOSE_PAREN ignore? statement elif_list | ;

//7.4 For statement
for_statement: FOR IDENTIFIER UNTIL expression BY expression ignore? statement;

//7.5 Break statement
break_statement: BREAK ignore;

//7.6 Continue statement
continue_statement: CONTINUE ignore;

//7.7 Return statement
return_statement: RETURN expression? ignore;

//7.8 Function call statement
call_statement: IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN ignore;

//7.9 Block statement
block_statement: BEGIN ignore block_list? END ignore;
block_list: statement block_list | statement;

//5. Expression
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | EQUAL_STRING | NOT_EQUAL | SMALLER | GREATER | SMALLER_EQUAL | GREATER_EQUAL) expression2 | expression2;
expression2: expression2 (AND_OP | OR_OP) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT_OP expression5 | expression6;
expression6: (ADD | SUB) expression6 | expression7;
expression7: (IDENTIFIER | IDENTIFIER OPEN_PAREN index_operator? CLOSE_PAREN) OPEN_BRACKET index_operator CLOSE_BRACKET | expression8;
expression8:  literals | IDENTIFIER | IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN | OPEN_PAREN expression CLOSE_PAREN;
literals: NUM_LIT | STRING_LIT | TRUE | FALSE | array_lit ;
array_lit: OPEN_BRACKET expression_list CLOSE_BRACKET;
expression_list: expression COMMA expression_list | expression;

// ignore character
ignore: NEWLINE+;

//3.4 Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var'; 
DYNAMIC: 'dynamic'; 
FUNC: 'func';
FOR: 'for';
UNTIL: 'until'; 
BY: 'by'; 
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if'; 
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

//3.5 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT_OP: 'not';
AND_OP: 'and';
OR_OP: 'or';
EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
SMALLER: '<';
SMALLER_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
CONCAT: '...';
EQUAL_STRING: '==';

//3.6 Seperators
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
COMMA: ',';

//3.3: Identifiers
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

//3.7 Literals

//Number
NUM_LIT: INTEGER DECIMAL? EXPONENT?;
fragment INTEGER: [0-9]+;
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: [eE] [+-]? [0-9]+;

//String
STRING_LIT: '"' (STRING_CHAR | ESCAPE)* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\r\n\\"];
fragment ESCAPE: '\\' [bfrnt'\\] | [']["];
fragment ILL_ESCAPE: '\\' ~[bfrnt'\\] | [\r];

//3.2 Comments
NEWLINE: '\n'; // newline
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments

WS: [ \t\b\f\r]+ -> skip ; // skip spaces, tabs, newlines

//Errors
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' (STRING_CHAR | ESCAPE)* (EOF | '\n' | '\r\n') {
	if self.text[-1] == '\n' and self.text[-2] == '\r':
		raise UncloseString(self.text[1:-2])
	elif self.text[-1] == '\n':
	    raise UncloseString(self.text[1:-1])
	else: 
	    raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' (STRING_CHAR | ESCAPE)* ILL_ESCAPE {
	raise IllegalEscape(self.text[1:])
};