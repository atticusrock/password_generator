import random

from flask import Flask, escape, request

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789!@#$%^&*'

def generator():
    password = ''.join(random.sample(symbols, len(symbols[0:16])))
    return password
print(generator())

app = Flask(__name__)

@app.route('/')
def password():
    name = request.args.get("name", "World")
    return generator()
1
1
1
1