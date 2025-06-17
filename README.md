PIZZA RESTAURANT API

---

ROUTES
//http://127.0.0.1:5000/restaurants
// http://127.0.0.1:5000/restaurants/:id
// http://127.0.0.1:5000/restaurants/:id
// http://127.0.0.1:5000/pizzas
// http://127.0.0.1:5000/restaurant_pizzas

---

OVERVIEW
This is a RESTful API for managing pizza restaurants, pizzas, and their relationships. It allows you to create, read, update, and delete (CRUD) restaurants, pizzas, and restaurant-pizza associations.

---

Installation

1. Clone the repository:

- git clone https://github.com/TechTinke/pizzas.git

2. Install dependencies:

- pipenv install

3. Activate the virtual environment:

- pipenv shell

4. Database Setup

- Initialize the database:
  export FLASK_APP=server.app:create_app
  flask db init
  flask db migrate -m "Initial migration"
  flask db upgrade

5. Seed the database:
   python server/seed.py
6. Start the Flask application:
   flask run

---

API ENDPOINTS

1. Restaurants

- GET /restaurants: List all restaurants.
- GET /restaurants/<int:id>: Get a restaurant by ID.
- DELETE /restaurants/<int:id>: Delete a restaurant by ID.

2. Pizzas

- GET /pizzas: List all pizzas.

3. Restaurant Pizzas

- POST /restaurant_pizzas: Create a new restaurant-pizza relationship.

---

EXAMPLE REQUESTS AND RESPONSES

1. GET /restaurants
   http://127.0.0.1:5000/restaurants
   Response:

[
{
"id": 1,
"name": "Mario's Pizza",
"address": "123 Pizza St"
},
{
"id": 2,
"name": "Kiki's Pizza",
"address": "456 Dough Ave"
}
]

2. GET /restaurants/:id
   http://127.0.0.1:5000/restaurants/1
   Response:

{
"id": 1,
"name": "Mario's Pizza",
"address": "123 Pizza St",
"pizzas": [
{
"id": 1,
"name": "Hawaiian",
"ingredients": "Pineapple, Ham, Cheese"
}
]
}

3. DELETE /restaurants/:id
   curl -X DELETE http://127.0.0.1:5000/restaurants/1
   Response:
   204 No Content

4. GET /pizzas
   curl http://127.0.0.1:5000/pizzas
   Response:

[
{
"id": 1,
"name": "Hawaiian",
"ingredients": "Pineapple, Ham, Cheese"
},
{
"id": 2,
"name": "Margherita",
"ingredients": "Tomatoes, Basil, Cheese"
}
]

5. POST /restaurant_pizzas
   curl -X POST -H "Content-Type: application/json" -d '{
   "price": 5,
   "pizza_id": 1,
   "restaurant_id": 3
   }' http://127.0.0.1:5000/restaurant_pizzas
   Success Response:

{
"id": 4,
"price": 5,
"pizza_id": 1,
"restaurant_id": 3,
"pizza": {
"id": 1,
"name": "Hawaiian",
"ingredients": "Pineapple, Ham, Cheese"
},
"restaurant": {
"id": 3,
"name": "Kiki's Pizza",
"address": "456 Dough Ave"
}
}
Error Response:

{
"errors": ["Price must be between 1 and 30"]
}
