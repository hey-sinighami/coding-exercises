"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

from collections import Counter

def ransom_note(magazine, ransom):
    return Counter(ransom) - Counter(magazine) == {}

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")


"""
Sample input:
6 4
give me one grand today night
give one grand today
Sample output:
Yes

Sample input:
6 5
two times three is not four
two times two is four
Sample output:
No
"""

