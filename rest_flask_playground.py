from flask import Flask, jsonify, request
import cashman.index
from cashman.index import get_incomes

print(get_incomes())

'''
app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]

@app.route("/")
def ping():
    return "PONG"

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204
#http://127.0.0.1:5000
#flask --app rest_flask_playground run
#https://auth0.com/blog/deve
'''
