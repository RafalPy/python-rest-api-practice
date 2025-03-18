import unittest
from index import ping, get_incomes
import requests

print(get_incomes())

class TestCashman(unittest.TestCase):

    def test_ping(self):
        self.assertEqual(ping(), "PONG")
    def test_ping_endpoint(self):

    # test_get_income(self):

    #def test_get_expense(self):

    #def test_post_income(self):

    #def test_post_expense(self):

if __name__ == '__main__':
    unittest.main()