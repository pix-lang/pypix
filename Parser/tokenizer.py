from .token import Token
from .token import token_names 

INTEGER, PLUS, MINUS, MULT, DIV, EOF = token_names


class Tokenizer:
    def __init__(self, text) -> None:
        self.text: str = text
        # Index of the text str
        self.pos = -0
        self.current_char = self.text[self.pos]
        # Current token instance
        self.current_token: Token = None


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
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        return int(result)


    def get_next_token(self) -> Token:
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULT, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)


    def eat(self, token_type: str):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()


    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term()
        while self.current_token.type in (PLUS, MINUS, MULT, DIV):
            if self.current_token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            if self.current_token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
            if self.current_token.type == MULT:
                self.eat(MULT)
                result *= self.term()
            if self.current_token.type == DIV:
                self.eat(DIV)
                result = result / self.term()

        return result



