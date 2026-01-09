from app import app
from models import db, Customer, Item, Review

with app.app_context():

    Customer.query.delete()
    Item.query.delete()
    Review.query.delete()

    c1 = Customer(name="Tal Yuri")
    c2 = Customer(name="Alex Kim")

    i1 = Item(name="Laptop Backpack", price=49.99)
    i2 = Item(name="Insulated Coffee Mug", price=9.99)

    r1 = Review(comment="Very durable", customer=c1, item=i1)
    r2 = Review(comment="Keeps drinks hot", customer=c1, item=i2)
    r3 = Review(comment="Great quality", customer=c2, item=i1)

    db.session.add_all([c1, c2, i1, i2, r1, r2, r3])
    db.session.commit()

    print("🌱 Database seeded!")
