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

                def eat(self, token_type):
                    if self.current_token.type == token_type:
                        self.current_token = next(self.lexer.get_next_token())
                    else:
                        self.error(f"Expected token {token_type}, got {self.current_token.type}")

    def if_statement(self):
        self.eat('IF')  # 'if'
        self.eat('LPAREN')  # '('
        self.expression()
        self.eat('RPAREN')  # ')'
        self.statement()
        if self.current_token.type == 'ELSE':
            self.eat('ELSE')
            self.statement()

    def while_statement(self):
        self.eat('WHILE')  # 'while'
        self.eat('LPAREN')  # '('
        self.expression()
        self.eat('RPAREN')  # ')'
        self.statement()

    def expression(self):
        # This method is simplified; real parsing of expressions is more involved
        self.simple_expression()
        if self.current_token.type in ['EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE']:
            self.rel_op()
            self.simple_expression()

    def simple_expression(self):
        self.term()
        while self.current_token.type in ['PLUS', 'MINUS']:
            self.add_op()
            self.term()

    def term(self):
        self.factor()
        while self.current_token.type in ['MUL', 'DIV']:
            self.mul_op()
            self.factor()

    def factor(self):
        if self.current_token.type == 'LPAREN':
            self.eat('LPAREN')
            self.expression()
            self.eat('RPAREN')
        elif self.current_token.type == 'NUMBER':
            self.eat('NUMBER')
        elif self.current_token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
        else:
            self.error()

    def rel_op(self):
        if self.current_token.type == 'EQ':
            self.eat('EQ')
        elif self.current_token.type == 'NEQ':
            self.eat('NEQ')
        # Add cases for LT, LTE, GT, GTE

    def add_op(self):
        if self.current_token.type == 'PLUS':
            self.eat('PLUS')
        elif self.current_token.type == 'MINUS':
            self.eat('MINUS')

    def mul_op(self):
        if self.current_token.type == 'MUL':
            self.eat('MUL')
        elif self.current_token.type == 'DIV':
            self.eat('DIV')
