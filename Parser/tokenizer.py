from Parser.token import Token, TokenType

operators = ["+", "-", "*", "/", ">"]
expr_operator_types = ["PLUS", "MINUS", "MULT", "DIV", "MODULO"]
cond_operators = [">", "<", "=="]
separators = [" ", "("]


class Tokenizer:
    def __init__(self, text) -> None:
        self.text: str = text
        # Index of the text str
        self.pos = -0
        self.current_char = self.text[self.pos]
        # Current token instance
        self.current_token: Token = Token("EOF", None)

    def error(self):
        raise Exception("Error while parsing input")

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while (self.current_char is not None) and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multi-digit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)

    def lexem(self, result):
        """Return a (multi-digit) lexem consumed from the input."""
        while self.current_char is not None and isinstance(self.current_char, str):
            result += self.current_char
            self.advance()

        return result

    @staticmethod
    def categorize(result):
        match result:
            case "if":
                return Token(TokenType.IF.name, TokenType.IF.value)
            case "def":
                return Token(TokenType.DEF.name, TokenType.DEF.value)
            case "func":
                return Token(TokenType.FUNC.name, TokenType.FUNC.value)
            case "while":
                return Token(TokenType.WHILE.name, TokenType.WHILE.value)
            case "for":
                return Token(TokenType.FOR.name, TokenType.FOR.value)

    def get_next_token(self) -> Token:
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token("INTEGER", self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS.name, TokenType.PLUS.value)

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS.name, TokenType.MINUS.value)

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULT.name, TokenType.MULT.value)

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV.name, TokenType.DIV.value)

            if self.current_char == "%":
                self.advance()
                return Token(TokenType.MODULO.name, TokenType.MODULO.value)

            if self.current_char == "=":
                result = ""
                while self.current_char == "=":
                    result += self.current_char
                    self.advance()

                match result:
                    case "=":
                        return Token(TokenType.EQUAL.name, TokenType.EQUAL.value)
                    case "==":
                        return Token(TokenType.DOUBLE_EQUAL.name, TokenType.DOUBLE_EQUAL.value)

            if self.current_char == ">":
                self.advance()
                return Token(TokenType.GREATER.name, TokenType.GREATER.value)

            if self.current_char == "<":
                self.advance()
                return Token(TokenType.LESSER.name, TokenType.LESSER.value)

            if self.current_char not in operators + separators:
                result = ""
                while self.current_char not in operators + separators:
                    result += self.current_char
                    self.advance()

                return self.categorize(result)

            self.error()

        return Token("EOF", None)

    def eat(self, token_type: str):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term_integer(self):
        token = self.current_token
        self.eat("INTEGER")

        return token.value

    def term(self, expected_type):
        token = self.current_token
        self.eat(expected_type)

        return token.value

    def expression(self, result):
        # Expected Pattern: [INTEGER, [OPERATOR, INTEGER]*]
        while self.current_token.type in expr_operator_types:
            match self.current_token.type:
                case TokenType.PLUS.name:
                    self.eat("PLUS")
                    result += self.term_integer()
                case TokenType.MINUS.name:
                    self.eat("MINUS")
                    result -= self.term_integer()
                case TokenType.MULT.name:
                    self.eat("MULT")
                    result *= self.term_integer()
                case TokenType.DIV.name:
                    self.eat("DIV")
                    result = result / self.term_integer()
                case TokenType.MODULO.name:
                    self.eat("MODULO")
                    result = result % self.term_integer()
        else:
            if self.current_token.type != TokenType.EOF.name:
                cond_operator = self.current_token.value
                match cond_operator:
                    case ">":
                        self.eat(TokenType.GREATER.name)
                    case "<":
                        self.eat(TokenType.LESSER.name)
                    case "==":
                        self.eat(TokenType.DOUBLE_EQUAL.name)

                result = self.condition(result, cond_operator)

        return result

    def condition(self, left, operator):
        # Expected Pattern: [INTEGER, OPERATOR, INTEGER]
        right = self.term(TokenType.INTEGER.name)

        cond = False
        match operator:
            case ">":
                cond = left > right
            case "<":
                cond = left < right
            case "==":
                cond = left == right
        return int(cond)

    def expr(self):
        # Pattern Expression : [INTEGER, [OPERATOR, INTEGER]*]
        # Pattern Function   : [FUNC, ID, ARG: [LPAREN, ARG*, RPAREN], EVAL: [LCURL, EXEC*, RCURL]]
        self.current_token = self.get_next_token()
        result = None

        if self.current_token.type == TokenType.INTEGER.name:
            result = self.term(TokenType.INTEGER.name)
            result = self.expression(result)
        elif self.current_token.type == TokenType.FUNC.name:
            result = self.term(TokenType.FUNC.name)

        return result
