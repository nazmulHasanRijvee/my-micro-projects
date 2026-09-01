# random password generator

print(f"\n{'Random':<{8}} {'Password':<{10}} {'Generator':<{10}}")

print("-" * 30)

import random

characters = [i for i in range(65, 122) if not (91 <= i <= 96)]

numbers = [i for i in range(48, 58)]

symbols = [
    i for i in range(33, 127) if not (48 <= i <= 57 or 65 <= i <= 90 or 97 <= i <= 122)
]


def operation(y, p, q):

    n, z, e, g, t, s, d, j = 0, 0, 0, 0, 0, 0, 0, 0

    if p == "yes":
        n = 1

    if q == "yes":
        z = 1

    if n == 1 and z == 1:
        e = int(y * 0.3)
        g = e
        j = e
        t = y - (2 * e)

    elif n == 1 or z == 1:
        e = int(y * 0.4)
        t = y - e

        if n == 1:
            g = e

        else:
            j = e

    return t, g, j


def shuffling(t, g, j):
    m = random.choices(characters, k=t)

    m += random.choices(numbers, k=g)

    m += random.choices(symbols, k=j)

    random.shuffle(m)

    return m


def check(x):

    if x not in ["yes", "no"]:
        print("\nOops invalid input. Please enter yes or no")
        return True


a = "\nDo you want to generate a password? (type yes or no) :- "

while True:
    x = input(a).lower()

    if check(x):
        continue

    else:
        if x == "yes":
            try:
                y = int(input("\nHow long do you want the password? :- "))
            except ValueError:
                print("\nOops invalid input. Please enter a number.")
                continue

            p = input("\nDo you want numbers in the password? :- ").lower()
            if check(p):
                continue

            q = input("\nDo you want symbols in the password? :- ").lower()
            if check(q):
                continue

            t, g, j = operation(y, p, q)

            m = shuffling(t, g, j)

            print("\nRandom password is :- ", end="")

            for i in m:
                print(chr(i), end="")

            a = "\n\nDo you want to generate another password? (type yes or no) :- "

        else:
            print("\nThank you for using this program")
            break
