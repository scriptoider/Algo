import random

def generateRandom(n):
    lis = []
    for _ in range(n):
        lis.append(random.randint(-100, 100))
    return lis
