from flask import Blueprint, render_template

payment = Blueprint('payment', __name__)

@payment.route('/payment')
def payment_page():

    return render_template('payment.html')