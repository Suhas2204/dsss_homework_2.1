import unittest
from math_quiz import yield_random_integers, yield_random_operators, perform_operation

class TestMathGame(unittest.TestCase):

    def test_yield_random_integers(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = yield_random_integers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_yield_random_operators(self):
        # Test if the random operator is one of the specified operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = yield_random_operators()
            self.assertIn(rand_operator, operators)

    def test_perform_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '*', '8 * 3', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
