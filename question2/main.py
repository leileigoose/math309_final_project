import numpy as np
import random


def kth(k):
    beds = [1, 2, 3, 4, 5, 6, 7]
    result = []
    result.append(random.choice(beds))

    for i in range(2, 8):
        if i not in result:
            result.append(i)
        else:
            r = set(result)
            b = set(beds)
            result.append(random.choice(list(b - r)))

    return k == result[k - 1]


c1, c2, c3, c4, c5, c6, c7 = 0, 0, 0, 0, 0, 0, 0

for i in range(100000):
    if kth(1):
        c1 += 1
    if kth(2):
        c2 += 1
    if kth(3):
        c3 += 1
    if kth(4):
        c4 += 1
    if kth(5):
        c5 += 1
    if kth(6):
        c6 += 1
    if kth(7):
        c7 += 1

result = [
    c1 / 100000,
    c2 / 100000,
    c3 / 100000,
    c4 / 100000,
    c5 / 100000,
    c6 / 100000,
    c7 / 100000,
]
for i in range(len(result)):
    print(
        "The probability of dwarf "
        + str(i + 1)
        + " sleeping in his own bed is %"
        + str(round(result[i] * 100, 2))
        + "."
    )
