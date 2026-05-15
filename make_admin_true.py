from app import app

from extensions import db

from models import User

with app.app_context():

    users = User.query.all()

    print("\nBEFORE UPDATE:\n")

    for user in users:

        print(user.email, user.is_admin)

    # FIND ADMIN USER
    admin = User.query.filter_by(
        email='admin@gmail.com'
    ).first()

    if admin:

        # FORCE ADMIN TRUE
        admin.is_admin = True

        db.session.commit()

        print("\nADMIN UPDATED SUCCESSFULLY!\n")

    else:

        print("\nADMIN USER NOT FOUND!\n")

    print("\nAFTER UPDATE:\n")

    users = User.query.all()

    for user in users:

        print(user.email, user.is_admin)