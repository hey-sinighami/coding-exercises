"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""
arr = [10, 20, 12, 13, 1, 4, 6, 2, 19, 5]
k1 = 15  # True
k2 = 40  # False
k3 = 12  # True
k4 = 76  # False
k5 = 1  # False
k6 = 10  # True
k7 = 0  # False

def has_sum(arr, k):
    sums = set()
    for num in arr:
        if num in sums:
            return True
        if num <= k:
            sums.add(k - num)
    return False

assert has_sum(arr, k1)
assert not has_sum(arr, k2)
assert has_sum(arr, k3)
assert not has_sum(arr, k4)
assert not has_sum(arr, k5)
assert has_sum(arr, k6)
assert not has_sum(arr, k7)



