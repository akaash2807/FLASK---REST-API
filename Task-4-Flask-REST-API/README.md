# Task 4 – Build a REST API with Flask

## Project Overview

This project is developed as part of the Python Developer Internship – Task 4.

The objective of this project is to create a REST API using Python and Flask to manage user data.

The API supports four HTTP methods: GET, POST, PUT, and DELETE. User information is stored in an in-memory Python dictionary.

## Technologies Used

- Python
- Flask
- REST API
- JSON
- Postman / cURL
- VS Code

## Features

- **GET:** Retrieve all users.
- **GET by ID:** Retrieve a specific user.
- **POST:** Add a new user.
- **PUT:** Update existing user details.
- **DELETE:** Remove a user.
- JSON-based request and response handling.
- Automatic user ID generation.
- Error handling for users that do not exist.
- HTTP status code handling.

## Project Structure

```text
Task-4-Flask-REST-API/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Install Python Packages

```bash
pip install -r requirements.txt
```

### Step 2: Run the Flask Application

```bash
python app.py
```

### Step 3: Open the API

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /users | Get all users |
| GET | /users/1 | Get a user by ID |
| POST | /users | Add a new user |
| PUT | /users/1 | Update a user |
| DELETE | /users/1 | Delete a user |

## Sample JSON Input

### POST – Add User

```json
{
    "name": "Hari",
    "email": "hari@example.com"
}
```

### PUT – Update User

```json
{
    "name": "Hari Updated",
    "email": "updated@example.com"
}
```

## HTTP Status Codes

- 200 – Request successful.
- 201 – User created successfully.
- 400 – Invalid request.
- 404 – User not found.

## Concepts Learned

- Flask Framework
- REST API Development
- HTTP Methods (GET, POST, PUT, DELETE)
- JSON Data Handling
- API Endpoints
- HTTP Status Codes
- Python Dictionaries
- Exception and Error Handling

## Conclusion

This project demonstrates how to develop a REST API using Python and Flask.

It provides basic user management functionality through GET, POST, PUT, and DELETE operations.

Through this task, I learned the fundamentals of REST API development, HTTP methods, JSON communication, and API testing.

---

**Python Developer Internship – Task 4**