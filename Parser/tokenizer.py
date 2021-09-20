import cython
from Cython.Build.Inline import cython_inline
from .token import Token
from .token import token_names 

INTEGER, PLUS, MINUS, EOF = token_names

@cython.cclass
class Tokenizer:
    def __init__(self, text) -> None:
        self.text: str = text
        # Index of the text str
        self.pos: cython.int = 0
        # Current token instance
        self.current_token: Token = None

    @cython.ccall
    def error(self):
        raise Exception("Error while parsing input")

    @cython.ccall
    def get_next_token(self) -> Token:
        # Returning None if reading further than text
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        current_char = self.text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1

            return token
        
        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos += 1

            return token
        
        if current_char == "-":
            token = Token(MINUS, current_char)
            self.pos += 1

            return token

        # 'return' keyword in Python ends the function
        # If nothing was returned, error will be raised 
        # Most likely due to Syntax Errors
        self.error()

    @cython.ccall
    def eat(self, token_type: str):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    @cython.ccall
    def expr(self) -> cython.int:
        self.current_token = self.get_next_token()

        left: cython.int = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right: cython.int = self.current_token
        self.eat(INTEGER)

        result: cython.int
        if op.type == PLUS:
            result = left.value + right.value
        if op.type == MINUS:
            result = left.value - right.value

        return result



