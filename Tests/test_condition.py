import unittest
from Parser.tokenizer import Tokenizer


class MyTestCase(unittest.TestCase):
    def expression_equal(self, tests: dict):
        """The "tests" dictionary contains an expression and the expected return value
        after parsing"""
        for line in tests:
            token_stream = Tokenizer(line)
            result = token_stream.expr()

            self.assertEqual(result, tests[line])

    def test_greater(self):
        tests = {
            "5 > 3": 1,
            "5 > 60": 0,
            "4000 > 5000": 0,

            "1>2": 0,
            "2   >   1": 1
        }

        self.expression_equal(tests)

    def test_lesser(self):
        tests = {
            "5 < 3": 0,
            "5 < 60": 1,
            "4000 < 5000": 1,

            "1<2": 1,
            "2    <    1": 0
        }

        self.expression_equal(tests)

