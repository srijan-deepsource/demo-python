import os

x = [i for i in range(10)]

def foo(x, y):
    if x > y:
        print(x)
    
    if x == y or x + 1 > y:
        print(y)
    
    if x + y == 42:
        return 42
