from app import app
from models.user import User

with app.app_context():

    users = User.query.all()

    print("=" * 60)
    print("REGISTERED USERS")
    print("=" * 60)

    for user in users:
        print(f"ID       : {user.id}")
        print(f"Username : {user.username}")
        print(f"Email    : {user.email}")
        print("-" * 60)