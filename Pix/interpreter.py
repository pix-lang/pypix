import sys
from Parser.tokenizer import Tokenizer

# py -m Pix.interpreter examples\hello.pix

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        code = f.readlines()
    for line in code:
        line = line.strip()
        token_stream = Tokenizer(line)
        result = token_stream.expr()

        print(result)

if __name__ == "__main__":
    main()

