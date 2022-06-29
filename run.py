from flask import Flask, render_template, request
from config import *


app = Flask(__name__)


@app.route('/main/<s>', methods=["GET", "POST"])
def main_route(s):
    return render_template("main.html", sidebar_components=sidebar_components, current=s, url_for_sidebar_components=url_for_sidebar_components, content=content[s])


@app.route('/enterbycode', methods=("GET", "POST"))
def sign_up_route():
    if request.method == "POST":
        return f"form: {request.form}"
    elif request.method == "GET":
        return render_template("enterbycode.html")


@app.route('/mailconfirmation', methods=("GET", "POST"))
def sign_in_route():
    if request.method == "POST":
        return f"form: {request.form}"
    elif request.method == "GET":
        return render_template("mailconfirmation.html")


app.debug = True

app.run("0.0.0.0") # pudge