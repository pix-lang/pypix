from Parser.token import Token
from Parser.pattern_matching import (if_statement,
                                     while_loop,
                                     condition_evaluation)

operators = ["PLUS", "MINUS", "MULT", "DIV"]
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

    def get_next_token(self) -> Token:
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token("INTEGER", self.integer())

            if self.current_char == '+':
                self.advance()
                return Token("PLUS", '+')

            if self.current_char == '-':
                self.advance()
                return Token("MINUS", '-')

            if self.current_char == '*':
                self.advance()
                return Token("MULT", '*')

            if self.current_char == '/':
                self.advance()
                return Token("DIV", '/')

            if self.current_char not in operators + separators:
                result = self.current_char
                self.advance()
                return Token("LEXEM", self.lexem(result))

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

    def term_lexem(self):
        token = self.current_token
        self.eat("LEXEM")

        return token.value

    def expression(self, result):
        while self.current_token.type in ("PLUS", "MINUS", "MULT", "DIV"):
            if self.current_token.type == "PLUS":
                self.eat("PLUS")
                result += self.term_integer()
            if self.current_token.type == "MINUS":
                self.eat("MINUS")
                result -= self.term_integer()
            if self.current_token.type == "MULT":
                self.eat("MULT")
                result *= self.term_integer()
            if self.current_token.type == "DIV":
                self.eat("DIV")
                result = result / self.term_integer()

        return result

    def categorize(self, result):
        current_char = ""
        i = 0

        while current_char not in separators + operators:
            current_char = result[i]
            i += 1

        statement = result[0:i-1]
        if statement == "if":
            ...

        print(condition_evaluation(if_statement, result))

        return result

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term_integer() if isinstance(self.current_token.value, int) else self.term_lexem()

        if isinstance(result, int):
            result = self.expression(result)
        elif isinstance(result, str):
            result = self.categorize(result)

        return result
