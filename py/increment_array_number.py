"""Given a non-empty array of non-negative integers, increment the number formed by the array members by one.
"""
arr1 = [1, 2, 3]
arr2 = [1, 2, 9]
arr3 = [9, 9, 9]
arr4 = [9]
arr5 = [0]

arr11 = [1, 2, 4]
arr22 = [1, 3, 0]
arr33 = [1, 0, 0, 0]
arr44 = [1, 0]
arr55 = [1]

def increment_array(arr):
    carry = 1
    idx = len(arr) - 1
    while carry:
        if arr[idx] == 9:
            arr[idx] = 0
            carry = 1
            if idx == 0:
                arr.insert(idx, 0)
                idx = 1
        else:
            arr[idx] += carry
            carry = 0
        idx -= 1

increment_array(arr1)
assert arr1 == arr11

increment_array(arr2)
assert arr2 == arr22

increment_array(arr3)
assert arr3 == arr33

increment_array(arr4)
assert arr4 == arr44

increment_array(arr5)
assert arr5 == arr55



