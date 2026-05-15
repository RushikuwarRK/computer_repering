from flask import Flask, render_template

from extensions import db, bcrypt, login_manager

app = Flask(__name__)

# SECRET KEY
app.config['SECRET_KEY'] = 'supersecretkey'

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# IMPORTANT SESSION FIX
app.config['SESSION_PERMANENT'] = False

app.config['SESSION_TYPE'] = 'filesystem'

# INIT
db.init_app(app)

bcrypt.init_app(app)

login_manager.init_app(app)

# LOGIN PAGE
login_manager.login_view = 'auth.login'

# IMPORT MODELS
from models import User

# LOAD USER
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

# IMPORT ROUTES
from routes.auth import auth
from routes.booking import booking
from routes.payment import payment
from routes.admin import admin

# REGISTER BLUEPRINTS
app.register_blueprint(auth)

app.register_blueprint(booking)

app.register_blueprint(payment)

app.register_blueprint(admin)

# HOME
@app.route('/')
def home():

    return render_template('index.html')

# RUN APP
if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)