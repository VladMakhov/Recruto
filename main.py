from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: str, message: str):
    return f'Hello {name}! {message}!'
