import unittest 
from Parser.tokenizer import Tokenizer

# py -m unittest Tests/test_expression.py

class TestExpression(unittest.TestCase):
    
    def expression_equal(self, tests: dict):
        '''The "tests" dictionary contains an expression and the expected return value 
        after parsing'''
        for line in tests:
            token_stream = Tokenizer(line)
            result = token_stream.expr()

            self.assertEqual(result, tests[line])


    def test_add(self):
        tests = {
            "10 + 5": 15,
            "1 + 1 + 1": 3,
            "1000 + 3": 1003
        }
        
        self.expression_equal(tests)


    def test_sub(self):
        tests = {
            "10 - 5": 5,
            "1 - 1 - 4": -4,
            "1000 - 300": 700
        }

        self.expression_equal(tests)


    def test_mult(self):
        tests = {
            "10 * 5": 50,
            "10 * 5 * 2": 100,
            "400 * 5": 2000,
        }

        self.expression_equal(tests)


    def test_div(self):
        tests = {
            "10 / 5": 2,
            "10 / 5 / 2": 1,
            "5 / 2": 2.5,
            "400 / 5": 80
        }

        self.expression_equal(tests)


    def test_all_operators(self):
        tests = {
            "10 * 5 - 3 / 3 + 1": 16.666666666666664,
            "10 / 5 * 2 + 3 - 8": -1,
            "400 - 3 * 10 + 4": 3974,
        }

        self.expression_equal(tests)

