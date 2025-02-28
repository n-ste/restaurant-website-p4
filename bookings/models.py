from bookings import db


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.reservation_name


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    customer_contact = db.Column(db.String, unique=True, nullable=False)
    customer_email = db.Column(db.String(50), unique=True, nullable=False)
    reservation_date = db.Column(db.DateTime, unique=True, nullable=False)

    def __repr__(self):
        return "First Name: {0} | Last Name: {1} | Mobile: {2} | Email: {3} | Reservation Date: {4}".format(
            self.first_name, self.last_name, self.customer_contact, self.customer_email, self.reservation_date
        )