from app import app

from extensions import bcrypt

from models import User

with app.app_context():

    user = User.query.filter_by(
        email='admin@gmail.com'
    ).first()

    print("\nEMAIL:", user.email)

    print("IS ADMIN:", user.is_admin)

    print(
        "PASSWORD MATCH:",
        bcrypt.check_password_hash(
            user.password,
            'admin123'
        )
    )