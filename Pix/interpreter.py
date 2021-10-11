import sys
from Parser.tokenizer import Tokenizer


# py -m Pix.interpreter Examples/hello.pix

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        # Read file and remove `\n`
        code = f.read().strip()

    token_stream = Tokenizer(code)
    result = token_stream.expr()

    print(result)


if __name__ == "__main__":
    main()
