import random

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789!@#$%^&*'

def generator():
    password = ''.join(random.sample(symbols, len(symbols[0:16])))
    return password