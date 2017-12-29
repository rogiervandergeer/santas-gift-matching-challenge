from numpy import array
from random import shuffle


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def random_solution():
    x = list(range(1000000))
    shuffle(x)
    return array(list(chunks(x, 1000)))


def generate_valid_solution():
    result = [[] for i in range(1000)]
    for i in range(5001):
        result[int(i/3)%1000].append(i)
    for i in range(5001, 45001):
        result[int((i+1)/2)%1000].append(i)
    row = 0
    for i in range(45001, 1000000):
        while len(result[row]) == 1000:
            row += 1
        result[row].append(i)
    return array(result)
