from flask import render_template
from bookings import app, db
from bookings.models import Reservation, Customer


@app.route("/")
def home():
    return render_template("bookings.html")
