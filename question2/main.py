import random


# Defines a function to put the kth dwarf
def kth(k):
    # Initializes the bed list
    beds = [1, 2, 3, 4, 5, 6, 7]
    # Initializes result of where dwarfs sleep
    result = []
    # Random choice for where dwarf 1 sleeps
    result.append(random.choice(beds))

    # For loop to see if the kth dwarfs bed is available
    for i in range(2, 8):
        # If available, dwarf gets put in his own bed
        if i not in result:
            result.append(i)
        # If not available dwarf gets put in a random bed that hasn't been chosen yet
        else:
            r = set(result)
            b = set(beds)
            result.append(random.choice(list(b - r)))
    # Returns true if kth dwarf is in his own bed, false otherwise
    return k == result[k - 1]


# Initializes number of occurrences of dwarfs 1-7 being in correct bed
c1, c2, c3, c4, c5, c6, c7 = 0, 0, 0, 0, 0, 0, 0

# Simulates selecting beds for each dwarf 100000 times
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

# List of probabilities of each dwarf selecting his own bed
result = [
    c1 / 100000,
    c2 / 100000,
    c3 / 100000,
    c4 / 100000,
    c5 / 100000,
    c6 / 100000,
    c7 / 100000,
]
# Print statement displaying results
for i in range(len(result)):
    print(
        "The probability of dwarf "
        + str(i + 1)
        + " sleeping in his own bed is %"
        + str(round(result[i] * 100, 2))
        + "."
    )
