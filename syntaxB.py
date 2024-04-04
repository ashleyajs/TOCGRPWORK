class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = next(self.lexer.get_next_token())

    def error(self, message="Invalid syntax"):
        raise Exception(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = next(self.lexer.get_next_token())
        else:
            self.error(f"Expected token {token_type}, got {self.current_token.type}")

    def program(self):
        # Program -> ClassDeclaration
        self.class_declaration()

    def class_declaration(self):
        # ClassDeclaration -> "class" Identifier "{" (MethodDeclaration | VariableDeclaration)* "}"
        self.eat('CLASS')
        self.eat('IDENTIFIER')  # Class name
        self.eat('LBRACE')
        while self.current_token.type in ['STATIC', 'INT', 'STRING']:
            if self.current_token.type == 'STATIC':
                self.method_declaration()
            else:  # 'INT', 'STRING'
                self.variable_declaration()
        self.eat('RBRACE')

    def method_declaration(self):
        # MethodDeclaration -> "static" ReturnType Identifier "(" Parameters ")" "{" Statement* "}"
        self.eat('STATIC')
        self.return_type()
        self.eat('IDENTIFIER')  # Method name
        self.eat('LPAREN')
        self.parameters()
        self.eat('RPAREN')
        self.eat('LBRACE')
        while self.current_token.type in ['IDENTIFIER', 'RETURN']:  # Simplified condition
            self.statement()
        self.eat('RBRACE')

    def variable_declaration(self):
        # VariableDeclaration -> Type Identifier ";"
        self.type()
        self.eat('IDENTIFIER')  # Variable name
        self.eat('SEMI')

    def return_type(self):
        # ReturnType -> "void" | Type
        if self.current_token.type in ['VOID', 'INT', 'STRING']:
            self.eat(self.current_token.type)  # 'VOID', 'INT', 'STRING'
        else:
            self.error()

    def type(self):
        # Type -> "int" | "String"
        if self.current_token.type in ['INT', 'STRING']:
            self.eat(self.current_token.type)
        else:
            self.error()

    def parameters(self):
        # Parameters -> Parameter ("," Parameter)* | ε
        if self.current_token.type in ['INT', 'STRING']:
            self.parameter()
            while self.current_token.type == 'COMMA':
                self.eat('COMMA')
                self.parameter()

    def parameter(self):
        # Parameter -> Type Identifier
        self.type()
        self.eat('IDENTIFIER')

    def statement(self):
        # Statement -> Expression ";" | ReturnStatement ";"
        if self.current_token.type == 'RETURN':
            self.return_statement()
        else:  # Assuming Expression starts with an IDENTIFIER
            self.expression()
        self.eat('SEMI')

    def return_statement(self):
        # ReturnStatement -> "return" Expression | "return"
        self.eat('RETURN')
        if self.current_token.type not in ['SEMI', 'RBRACE']:
            self.expression()

    # Expression, Term, and Factor methods would follow similar logic to previous explanations,
    # handling arithmetic expressions and parentheses.

    # Placeholder for Expression, Term, Factor as their implementation depends on specific tokens
    # and operations defined in the Lexer.
