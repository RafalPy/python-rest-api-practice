

from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]



@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204
#http://127.0.0.1:5000
#flask --app hello run
#https://auth0.com/blog/deve
