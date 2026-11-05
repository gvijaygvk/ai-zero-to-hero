"""Module 2 · Lesson 1 — your first FastAPI endpoints."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}"}


@app.get("/add")
def add(a: int, b: int = 0):
    return {"a": a, "b": b, "sum": a + b}


@app.get("/square/{n}")
def square(n: int, negate: bool = False):
    if negate == True:
        return {"n": n, "square": -n * n}
    else:
        return {"n": n, "square": n * n}
