from app import app
import lounaat
import users
from flask import redirect, render_template, request, session
from datetime import date, datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash


@app.route("/")
def index():
    ravintolat = lounaat.hae_ravintolat()
    lounaat_tanaan= lounaat.hae_lounaat_tanaan()
    return render_template("index.html",ravintolat=ravintolat, lounaat=lounaat_tanaan)

@app.route("/ravintola/<int:id>")
def ravintolat(id):
    ravintola = lounaat.hae_ravintola(id)
    ravintolan_lounaat = lounaat.hae_ravintolan_lounaat(id)
    tanaan = date.today().strftime("%Y-%m-%d")
    huomenna = date.today() + timedelta(days=1)
    huomenna = huomenna.strftime("%Y-%m-%d")

    return render_template("ravintola.html", id=id, ravintola=ravintola, lounaat=ravintolan_lounaat, tanaan=tanaan, huomenna=huomenna)

@app.route("/kirjautuminen")
def kirjautuminen():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    #TODO: check username & password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"] 
    return redirect("/")   
