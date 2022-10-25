import math


def sieve_of_eratosthenes(n):
    if n < 1:
        raise ValueError(f'Invalid input please provide a number larger than 1. Number: {n}.')

    sv = [True] * (n + 1)
    pm = []
    st = 2
    ed = int(math.sqrt(n))

    while st <= ed:
        if sv[st] is True:
            pm.append(st)

            for i in range(st * st, n + 1, st):
                if sv[i] is True:
                    sv[i] = False

        st += 1

    for j in range(ed + 1, n + 1):
        if sv[j] is True:
            pm.append(j)

    return pm

print(sieve_of_eratosthenes(13))  # [2, 3, 5, 7, 11, 13]
print(sieve_of_eratosthenes(7))  # [2, 3, 5, 7]
print(sieve_of_eratosthenes(24))  # [2, 3, 5, 7, 11, 13, 17, 19, 23]

