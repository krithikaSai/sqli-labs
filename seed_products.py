from app import app, db
from models.db import Product

with app.app_context():
    products = [
        Product(name="Hacker Hoodie", price=799.00, description="Boosts stealth and terminal speed."),
        Product(name="Firewall Fries", price=129.00, description="Fiery enough to block intrusions."),
        Product(name="Trojan Tea", price=99.00, description="Looks innocent, acts otherwise."),
        Product(name="Packet Popcorn", price=89.00, description="Sniff-worthy with every bite."),
        Product(name="SQLi Strawberry Shake", price=199.00, description="Insert flavor into your mouth OR 1=1."),
        Product(name="Keylogger Keyboard", price=899.00, description="Type like a pro, record like a spy."),
        Product(name="Obfuscation Sunglasses", price=349.00, description="Hide your eyes. Reveal nothing."),
        Product(name="Zero-Day Donuts", price=159.00, description="Found in the wild. Not patched."),
        Product(name="Dark Web Mug", price=249.00, description="One sip, and you're on a watchlist."),
        Product(name="Backdoor Backpack", price=999.00, description="Stores gear and secrets alike."),
        Product(name="Cache Cookies", price=119.00, description="Stored locally for instant joy."),
        Product(name="Script Kiddie Samosa", price=20.00, description="No skills, all flavor."),
        Product(name="Privilege Escalator Toy", price=299.00, description="Grants root... in imagination only."),
    ]

    db.session.add_all(products)
    db.session.commit()
    print("✅ Products seeded successfully!")
