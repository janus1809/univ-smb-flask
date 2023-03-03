# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")

@app.route("/filter")
def rules_filter():
    return ""

@app.route("/nat")
def rules_nat():
    return ""

@app.route("/add")
def rules_nat_add():
    return ""

@app.route("/alias")
def alias():
    return ""