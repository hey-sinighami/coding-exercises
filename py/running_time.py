"""Running Time and Complexity
https://www.hackerrank.com/challenges/30-running-time-and-complexity
"""

def is_prime(num):
    if num == 2:
        return True
    elif num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    num = int(input())
    print("Prime" if is_prime(num) else "Not prime")

"""
Sample Input:
3
12
5
7
Sample Output:
Not prime
Prime
Prime
"""

