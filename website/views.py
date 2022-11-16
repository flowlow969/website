from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/CV')
def CV():
    return render_template("CV.html")

@views.route('/Portfolio')
def Portfolio():
    return render_template("Portfolio.html")

@views.route('/Kontakt')
def Kontakt():
    return render_template("Kontakt.html")
