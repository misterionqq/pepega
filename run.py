
from flask import Flask, render_template, request, flash
import flask
from config import *


app = Flask(__name__)
app.secret_key = b"poqwjahfdpih"


@app.route('/main/<s>', methods=["GET", "POST"])
def main_route(s):
    return render_template("main.html", sidebar_components=sidebar_components, current=s, url_for_sidebar_components=url_for_sidebar_components, content=content[s])


@app.route("/auth/<s>", methods=("GET", "POST"))
def auth_route(s):
    if request.method == "POST":
        flash("Message"+" mes"*25, "error")
    return render_template(s+".html")


@app.route('/enterbycode', methods=("GET", "POST"))
def sign_up_route():
    if request.method == "POST":    
        return f"form: {request.form}"
    elif request.method == "GET":
        return render_template("enterbycode.html")


@app.route('/enterbymail', methods=("GET", "POST"))
def enter_by_mail_route():
    if request.method == "POST":    
        return f"form: {request.form}"
    elif request.method == "GET":
        return render_template("enterbymail.html")


@app.route('/mailconfirmation', methods=("GET", "POST"))
def sign_in_route():
    if request.method == "POST":
        flash("Письмо отправленно к вам на почту", "error")
        return render_template("mailconfirmation.html")
        #return f"form: {request.form}"
    elif request.method == "GET":
        return render_template("mailconfirmation.html")


@app.route('/passwordchange', methods=("GET", "POST"))
def pass_change_route():
    if request.method == "GET":
        return render_template("passwordchange.html")
    elif request.method == "POST":
        flash("Messge mes"+" mes"*25, "error")
        return render_template("passwordchange.html")


app.debug = True

app.run("0.0.0.0") # pudge