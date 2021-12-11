#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(line.strip())

# with open("input.txt") as file:
#     inp = file.read().strip()

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
other = {')': '(', '}': '{', ']': '[', '>': '<'}
ans = 0
noncorrupted = []
for line in arr:
    stack = []
    for c in line:
        if c in ['(', '{', '[', '<']:
            stack.append(c)
        else:
            
            if other[c] != stack[-1]:
                ans += points[c]
                break
            curr = stack.pop()
    else:
        noncorrupted.append(line)
print(ans)
points = {'(': 1, '[': 2, '{': 3, '<': 4}
other = {')': '(', '}': '{', ']': '[', '>': '<'}
ans = []

for line in noncorrupted:
    stack = []
    for c in line:
        if c in ['(', '{', '[', '<']:
            stack.append(c)
        else:
            if stack:
                stack.pop()
    bal = 0
    for c in reversed(stack):
        bal *= 5
        bal += points[c]
    ans.append(bal)
print(sorted(ans))
print(list(sorted(ans))[len(ans)//2])

