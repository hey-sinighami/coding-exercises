"""Given the expected and actual return dates for a library book, create a program that calculates the fine (if any).

https://www.hackerrank.com/challenges/30-nested-logic/problem

"""

from datetime import date

def fine(ret_date, exp_date):
    if ret_date <= exp_date:
        return 0
    elif ret_date.year == exp_date.year:
        if ret_date.month == exp_date.month:  # same calendar month
            return 15 * (ret_date - exp_date).days
        else:  # after the current calendar month
            return 500 * (ret_date.month - exp_date.month)
    else:
        return 10000

ret = [i for i in map(int, input().split(' '))]
exp = [i for i in map(int, input().split(' '))]

ret_date = date(ret[2], ret[1], ret[0])
exp_date = date(exp[2], exp[1], exp[0])
print(fine(ret_date, exp_date))

"""
Sample input:
9 6 2015
6 6 2015

Sample output:
45
"""

