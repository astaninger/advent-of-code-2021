#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(list(map(int, list(line.strip()))))

def flash(i, j):
    # print(i, j, hasFlashed)
    if (i, j) in hasFlashed:
        return 0
    myAns = 1
    hasFlashed.add((i, j))
    for x in [i-1, i, i+1]:
        for y in [j - 1, j, j+1]:
            if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                arr[x][y] += 1
                if arr[x][y] > 9 and (x,y) not in hasFlashed:
                    myAns += flash(x, y)
    return myAns
lastAns = 0
ans = 0
for _ in range(100):
    hasFlashed = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 9 and (i, j):
                ans += flash(i, j)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 9:
                arr[i][j] = 0

print(ans)

step = 100
while (ans - lastAns) != len(arr)*len(arr[0]):
    step += 1
    hasFlashed = set()
    lastAns = ans
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 9 and (i, j):
                ans += flash(i, j)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 9:
                arr[i][j] = 0

print(step)