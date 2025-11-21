import unittest
from Problem1 import solve_problem

class TestHidden1(unittest.TestCase):
    def test_solve_problem(self):
        try:
            solve_problem()
        except Exception as e:
            self.fail(f"solve_problem() raised an exception {e}")