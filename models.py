from extensions import db

from flask_login import UserMixin


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )

    # ADMIN ROLE
    is_admin = db.Column(
        db.Boolean,
        default=False
    )


class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    phone = db.Column(db.String(100))

    service = db.Column(db.String(100))

    date = db.Column(db.String(100))

    message = db.Column(db.Text)


class Payment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    customer_name = db.Column(db.String(100))

    payment_method = db.Column(db.String(100))

    amount = db.Column(db.String(100))

    transaction_id = db.Column(db.String(200))