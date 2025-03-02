from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello, World!"

@app.route("/bonjour")
def bonjour_word():
    return "Bonjour, World!"



#http://127.0.0.1:5000
#flask --app hello run
#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/