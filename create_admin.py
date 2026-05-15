from app import app

from extensions import db, bcrypt

from models import User

with app.app_context():

    # CREATE TABLES
    db.create_all()

    # HASH PASSWORD
    hashed_password = bcrypt.generate_password_hash(
        'admin123'
    ).decode('utf-8')

    # CREATE ADMIN USER
    admin = User(

        username='admin',

        email='admin@gmail.com',

        password=hashed_password,

        is_admin=True
    )

    db.session.add(admin)

    db.session.commit()

    print("ADMIN CREATED SUCCESSFULLY")