#!/bin/python3
"""Find the Running Median using Heaps
https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
"""

import sys
from bisect import bisect
from math import ceil

def print_running_medians(aas):
    sorted_arr = []
    for a in aas:
        sorted_arr.insert(bisect(sorted_arr, a), a)
        l = len(sorted_arr)
        if l % 2 == 0:
            median = (sorted_arr[l//2] + sorted_arr[(l//2)-1]) / 2
        else:
            median = sorted_arr[ceil(l//2)] / 1  # to make result float
        print(median)


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

print_running_medians(a)


"""
Sample input:
6
12
4
5
3
8
7
Sample output:
12.0
8.0
5.0
4.5
5.0
6.0

"""

