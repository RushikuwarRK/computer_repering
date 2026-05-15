from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from extensions import db, bcrypt

from models import User

auth = Blueprint('auth', __name__)


# REGISTER
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']

        email = request.form['email']

        password = request.form['password']

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash('Email already exists')

            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

        user = User(

            username=username,

            email=email,

            password=hashed_password,

            is_admin=False
        )

        db.session.add(user)

        db.session.commit()

        flash('Registration Successful')

        return redirect('/login')

    return render_template('register.html')


# LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():

    # IF ALREADY LOGGED IN
    if current_user.is_authenticated:

        if current_user.is_admin:

            return redirect('/dashboard')

        return redirect('/')

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):

            # IMPORTANT SESSION LOGIN
            login_user(user, remember=True)

            flash('Login Successful')

            # ADMIN
            if user.is_admin:

                return redirect('/dashboard')

            # NORMAL USER
            return redirect('/')

        flash('Invalid Email or Password')

    return render_template('login.html')


# LOGOUT
@auth.route('/logout')
@login_required
def logout():

    logout_user()

    flash('Logged Out Successfully')

    return redirect('/login')