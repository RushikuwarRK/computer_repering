from flask import Blueprint, render_template, redirect

from flask_login import (
    login_required,
    current_user
)

from models import (
    User,
    Booking,
    Payment
)

admin = Blueprint('admin', __name__)


@admin.route('/dashboard')
@login_required
def dashboard():

    # DEBUG
    print("AUTH:", current_user.is_authenticated)

    print("ADMIN:", current_user.is_admin)

    # CHECK ADMIN
    if not current_user.is_admin:

        return redirect('/')

    users = User.query.all()

    bookings = Booking.query.all()

    payments = Payment.query.all()

    return render_template(
        'admin.html',
        users=users,
        bookings=bookings,
        payments=payments
    )