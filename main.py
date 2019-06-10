import random

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789!@#$%^&*'
password = ''.join(random.sample(symbols,len(symbols[0:16])))

print(password)