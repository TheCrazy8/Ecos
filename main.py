import datetime
import sys
import os
import math
import random

now = datetime.datetime.now()
pi = math.pi
e = math.e
rand_num = random.randint(1, 100)
namespace = os.getenv('USER', 'Guest')

def greet_user(name):
    return f"Hello, {name}! Today is {now.strftime('%Y-%m-%d')}."

def main():
    print(greet_user(namespace))
