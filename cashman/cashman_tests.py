import unittest
from index import ping, get_incomes
import requests
import json

#Run the Flask app before running the tests

class TestCashman(unittest.TestCase):

    def test_ping(self):
        self.assertEqual(ping(), "PONG")
    def test_ping_endpoint(self):
        response = requests.get("http://localhost:5000/")
        self.assertEqual(response.text, "PONG")
    def test_get_income(self):
        expected = [{"amount":5000.0,"created_at":"2025-03-18","description":"Salary","type":"TransactionType.INCOME"},{"amount":200.0,"created_at":"2025-03-18","description":"Dividends","type":"TransactionType.INCOME"}]
        response = requests.get("http://localhost:5000/incomes")
        self.assertEqual(response.status_code, 200)
        actual = json.loads(response.text)  # Converts response to Python list/dict
        self.assertEqual(json.dumps(actual, sort_keys=True), json.dumps(expected, sort_keys=True))
    def test_get_expense(self):
        expected = [{"amount":-50.0,"created_at":"2025-03-18","description":"pizza","type":"TransactionType.EXPENSE"},{"amount":-100.0,"created_at":"2025-03-18","description":"Rock Concert","type":"TransactionType.EXPENSE"}]
        response = requests.get("http://localhost:5000/expenses")
        self.assertEqual(response.status_code, 200)
        actual = json.loads(response.text)  # Converts response to Python list/dict
        self.assertEqual(json.dumps(actual, sort_keys=True), json.dumps(expected, sort_keys=True))
    def test_post_income(self):
        first_response = requests.get("http://localhost:5000/incomes")
        self.assertEqual(first_response.status_code, 200)
        expected = json.loads(first_response.text) #plus tu damy nasz post
        requests.post("http://localhost:5000/incomes", headers={"Content-Type": "application/json"}, json=  {"amount": 300.0, "description": "loan payment"} )
        second_response = requests.get("http://localhost:5000/incomes")
        actual = json.loads(second_response.text)

        #def test_post_expense(self):

if __name__ == '__main__':
    unittest.main()