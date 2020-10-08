import random


def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    print([random.random() * 5 + 30 for i in range(10)])
