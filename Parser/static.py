"""
This Python file has the static functions that the Tokenizer would normally use.
"""
from Parser.token import Token, TokenType


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

