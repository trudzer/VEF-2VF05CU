from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Halló Heimur"
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/two">sida 2</a>
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/home/three">sida 3</a>
    

@app.route("/two")
def two():
    return "Hello, two!"
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/">sida 1</a>
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/home/three">sida 3</a>

@app.route("/home/three")
def homethree():
    return "Hello, three!"
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/">sida 1</a>
    <a href="https://vefth2vf0-verkefni2.herokuapp.com/two">sida 2</a>
