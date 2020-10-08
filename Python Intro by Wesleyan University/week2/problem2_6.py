import random

def problem2_6():
    random.seed(431)
    for i in range(100):
        print(random.randint(1, 6) + random.randint(1, 6))


