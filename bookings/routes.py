from flask import render_template, request, redirect, url_for
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
    reservation = list(Reservation.query.order_by(Reservation.reservation_name).all())
    return render_template("reservations.html", reservations=reservation)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/add_booking", methods=["GET", "POST"])
def add_booking():
    if request.method == "POST":
        booking = Reservation(reservation_name=request.form.get("reservation_name"))
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for("bookings"))
    return render_template("add-booking.html")
