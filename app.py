from flask import Flask
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Halló Heimur"

@app.route("/two")
def two():
    return "Hello, two!"

@app.route("/home/three")
def homethree():
    return "Hello, three!"
