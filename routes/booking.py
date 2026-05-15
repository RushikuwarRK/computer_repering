from flask import Blueprint, render_template, request

from extensions import db

from models import Booking

booking = Blueprint('booking', __name__)

@booking.route('/booking', methods=['GET', 'POST'])
def booking_page():

    if request.method == 'POST':

        new_booking = Booking(

            name=request.form['name'],

            service=request.form['service'],

            date=request.form['date'],

            message=request.form['message']
        )

        db.session.add(new_booking)

        db.session.commit()

    return render_template('booking.html')