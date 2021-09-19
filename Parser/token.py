token_names = [
    "INTEGER",
    "PLUS",
    "MINUS",
    "EOF"
]

class Token:
    def __init__(self, type: str, value) -> None:
        '''
        Type can be any of the token names
        Value can be any char
        '''
        self.type = type
        self.value = value

    
    def __str__(self) -> str:
        # Example: Token(INTEGER, 3)

        return f"Token({self.type}, {self.value})"

    
    # Good to have both methods,
    # Defaults to other if one is not present
    def __repr__(self) -> str:
        return f"Token(type={self.type!r}, value={self.value!r})"



