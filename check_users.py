from app import app

from models import User

with app.app_context():

    users = User.query.all()

    print("\nALL USERS:\n")

    for user in users:

        print(
            "ID:", user.id,
            "| EMAIL:", user.email,
            "| ADMIN:", user.is_admin
        )