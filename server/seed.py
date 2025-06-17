# server/seed.py
from server.app import create_app
from server.extensions import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

def seed_db():
    # Restaurants
    restaurant1 = Restaurant(name="Mario's Pizza", address="123 Pizza St")
    restaurant2 = Restaurant(name="Kiki's Pizza", address="456 Dough Ave")
    
    # Pizzas
    pizza1 = Pizza(name="Hawaiian", ingredients="Pineapple, Ham, Cheese")
    pizza2 = Pizza(name="Margherita", ingredients="Tomatoes, Basil, Cheese")
    
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        seed_db()