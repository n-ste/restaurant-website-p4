from flask import render_template
from bookings import app, db
from bookings.models import Reservation, Customer


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/bookings")
def bookings():
    return render_template("reservations.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
