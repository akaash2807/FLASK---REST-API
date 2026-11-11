
from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

# In-memory dictionary to store users
users = {}

# Generate user IDs
next_user_id = 1


# HOME ROUTE
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Flask REST API",
        "available_routes": {
            "GET": "/users",
            "POST": "/users",
            "GET_SINGLE_USER": "/users/<id>",
            "PUT": "/users/<id>",
            "DELETE": "/users/<id>"
        }
    }), 200


# GET - Display all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "message": "Users retrieved successfully",
        "users": list(users.values())
    }), 200


# GET - Display a single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    if user_id not in users:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "message": "User retrieved successfully",
        "user": users[user_id]
    }), 200


# POST - Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    global next_user_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Please provide valid JSON data"
        }), 400

    name = data.get("name")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "Name is required"
        }), 400

    if not isinstance(email, str) or not email.strip():
        return jsonify({
            "error": "Email is required"
        }), 400

    user = {
        "id": next_user_id,
        "name": name.strip(),
        "email": email.strip()
    }

    users[next_user_id] = user
    next_user_id += 1

    return jsonify({
        "message": "User added successfully",
        "user": user
    }), 201


# PUT - Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    if user_id not in users:
        return jsonify({
            "error": "User not found"
        }), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({
            "error": "Please provide valid JSON data"
        }), 400

    if "name" in data:
        if not isinstance(data["name"], str) or not data["name"].strip():
            return jsonify({
                "error": "Name cannot be empty"
            }), 400

    if "email" in data:
        if not isinstance(data["email"], str) or not data["email"].strip():
            return jsonify({
                "error": "Email cannot be empty"
            }), 400

    if "name" in data:
        users[user_id]["name"] = data["name"].strip()

    if "email" in data:
        users[user_id]["email"] = data["email"].strip()

    return jsonify({
        "message": "User updated successfully",
        "user": users[user_id]
    }), 200


# DELETE - Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    if user_id not in users:
        return jsonify({
            "error": "User not found"
        }), 404

    deleted_user = users.pop(user_id)

    return jsonify({
        "message": "User deleted successfully",
        "user": deleted_user
    }), 200


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
