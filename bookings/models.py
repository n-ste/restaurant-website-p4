from bookings import db


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_name = db.Column(db.String(75), unique=True, nullable=False)
    customer = db.relationship("Customer", backref="reservation", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.reservation_name


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_reservation = db.Column(db.String(75), unique=True, nullable=False)
    customer_name = db.Column(db.Text, nullable=False)
    reservation_date = db.Column(db.DateTime, unique=True, nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Customer: {1}".format(
            self.id, self.customer_reservation
        )
