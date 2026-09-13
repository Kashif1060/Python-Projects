%%writefile app.py

from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App")


# Home page
@app.get("/")
def home():
    return {
        "message": "Welcome to My FastAPI App!",
        "status": "API is working"
    }


# Greet a user
@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!",
        "welcome": "Nice to meet you!"
    }


# Multiply two numbers
@app.get("/multiply")
def multiply(a: int, b: int):
    return {
        "first_number": a,
        "second_number": b,
        "result": a * b
    }



# User information
@app.get("/user")
def user(name: str, age: int, city: str):
    return {
        "name": name,
        "age": age,
        "city": city
    }
