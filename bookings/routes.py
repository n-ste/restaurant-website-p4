from flask import render_template, request, redirect, url_for
from bookings import app, db
from bookings.models import Reservation, Customer


@app.route("/")
def home():
    customers = list(Customer.query.order_by(Customer.reservation_date).all())
    return render_template("index.html", customers=customers)

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
    return render_template("add_booking.html")


@app.route("/amend_booking/<int:reservation_id>", methods=["GET", "POST"])
def amend_booking(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if request.method == "POST":
        reservation.reservation_name = request.form.get("reservation_name")
        db.session.commit()
        return redirect(url_for("bookings"))
    return render_template("amend_booking.html", reservation=reservation)


@app.route("/delete_reservation/<int:reservation_id>")
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return redirect(url_for("bookings"))


@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    reservation = list(Reservation.query.order_by(Reservation.reservation_name).all())
    if request.method == "POST":
        customer = Customer(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            customer_contact=request.form.get("customer_contact"),
            customer_email=request.form.get("customer_email"),
            reservation_date=request.form.get("reservation_date"),
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("bookings"))
    return render_template("add_customer.html", reservation=reservation)