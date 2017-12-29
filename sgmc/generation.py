from numpy import array
from random import shuffle, randint


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def random_valid_solution():
    result = [[] for _ in range(1000)]
    for i, j, k in zip(range(5001, 3), range(1, 5001, 3), range(2, 5001, 3)):
        result[randint(0, 999)] += [i, j, k]
    for i, j in zip(range(5001, 45001, 2), range(5002, 45001, 2)):
        result[randint(0, 999)] += [i, j]
    for row in result:
        assert len(row) <= 1000
    row = 0
    for i in range(45001, 1000000):
        while len(result[row]) == 1000:
            row += 1
        result[row].append(i)
    return array(result)


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



