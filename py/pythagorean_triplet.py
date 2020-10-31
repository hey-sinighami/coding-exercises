"""Given an array of integers, determine whether it contains a Pythagorean triplet.
"""


def has_triplet_v1(arr):
    """Returns ``True`` if array ``arr`` contains a Pythagorean Triplet, ``False`` otherwise.
    """

    j = 0
    n = len(arr)
    for i in range(n - 2):
        for k in range(j + 1, n):
            for j in range(i + 1, n - 1):
                x = arr[i] * arr[i]
                y = arr[j] * arr[j]
                z = arr[k] * arr[k]
                if (x == y + z) or (y == x + z) or (z == x + y):
                    return True


    return False


def has_triplet_v2(arr):
    """A better approach to find Pythagorean triplets in O(n^2) time.
    """

    n = len(arr)

    arr.sort()

    for i in range(n):
        arr[i] = arr[i] * arr[i]

    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            else:
                if arr[j] + arr[k] < arr[i]:
                    j = j + 1
                else:
                    k = k -1

    return False



arr = [3, 1, 4, 5, 6]
assert(has_triplet_v1(arr))  # 3, 4, 5
assert(has_triplet_v2(arr))  # 3, 4, 5

arr = [13, 12, 4, 5, 6]
assert(has_triplet_v1(arr))  # 5, 12, 13
assert(has_triplet_v2(arr))  # 5, 12, 13

arr = [33, 11, 7, 5, 6]
assert(not has_triplet_v1(arr))
assert(not has_triplet_v2(arr))

arr = [7, 0, 24, 25, 36]
assert(has_triplet_v1(arr))  # 7, 24, 25
assert(has_triplet_v2(arr))  # 7, 24, 25

arr = [10, 4, 6, 12, 5]
assert(not has_triplet_v1(arr))
assert(not has_triplet_v2(arr))

 

