# server/models/pizza.py
from server.extensions import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', cascade="all, delete-orphan")