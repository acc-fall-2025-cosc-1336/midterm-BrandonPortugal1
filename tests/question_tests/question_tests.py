import unittest

# Question A
from src.question_a.question_a import test_config, is_prime

# Question B
from src.question_b.question_b import get_miles_per_hour

# Question C
from src.question_c.question_c import get_day_of_week

# Question D
from src.question_d.question_d import get_bonus_pay_amount

class Test_Config(unittest.TestCase):
    def test_question_a_config(self):
        self.assertEqual(True, test_config())

class TestQuestionA(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))

class TestQuestionB(unittest.TestCase):
    def test_get_miles_per_hour(self):
        self.assertEqual(get_miles_per_hour(32, 60), 19.883872)
        self.assertEqual(get_miles_per_hour(-5, 30), "Invalid arguments")
        self.assertEqual(get_miles_per_hour(10, -1), "Invalid arguments")

class TestQuestionC(unittest.TestCase):
    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")

class TestQuestionD(unittest.TestCase):
    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000), 70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid arguments")

if __name__ == '__main__':
    unittest.main()




