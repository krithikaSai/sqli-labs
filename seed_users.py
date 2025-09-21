from werkzeug.security import generate_password_hash
from models.db import db, User
from app import app

with app.app_context():
    # Hashing passwords before inserting into the database
    hashed_password_admin = generate_password_hash('adminpassword')
    hashed_password_player1 = generate_password_hash('player1password')
    hashed_password_h4x0r = generate_password_hash('h4x0rpassword')

    # Create user instances with hashed passwords
    user1 = User(username='admin', email='admin@ctf.com', is_admin=True, password_hash=hashed_password_admin)
    user2 = User(username='player1', email='player1@ctf.com', is_admin=False, password_hash=hashed_password_player1)
    user3 = User(username='h4x0r', email='leet@hacks.com', is_admin=False, password_hash=hashed_password_h4x0r)

    # Add users to session and commit
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    print("✅ Users seeded successfully.")
