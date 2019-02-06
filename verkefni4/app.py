from flask import Flask, render_template, url_for, json, request, flash, redirect
import os
import urllib.request

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/currecy/") as url:
    data = json.loads(url.read().decode())

@app.route("/")
def index():
    return render_template('index.tpl', data=data)

if __name__ == "__main__":
    app.run()
