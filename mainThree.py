import random


def count_pi(n):
    i = 0
    count = 0
    while i < n:
        x = random.random()
        y = random.random()
        if (pow(x, 2) + pow(y, 2)) < 1:
            count += 1
        i += 1
    return 4 * (count / n)


pi = count_pi(100000)
print(pi)
