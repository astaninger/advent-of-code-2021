#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(line.strip())
arr[0] = arr[0].split(': ')[1]
x, y = arr[0].split(', ')
xStart, xEnd = x.split('..')
xStart = int(xStart[2:])
xEnd = int(xEnd)
yStart, yEnd = y.split('..')
yStart = int(yStart[2:])
yEnd = int(yEnd)
pos = [0, 0]
ans = []
maxY = float('-inf')
for x in range(xEnd+1):
    for y in range(min(-yEnd, yEnd, yStart, -yStart), max(yEnd, -yEnd, yStart, -yStart)):
        currMaxY = float("-inf")
        myX = x
        myY = y
        while pos[0] <= xEnd and pos[1] >= yStart:
            pos[0] += myX
            pos[1] += myY
            myX += (-1 if myX > 0 else 1) if myX != 0 else 0
            myY += -1
            currMaxY = max(currMaxY, pos[1])
            if xStart <= pos[0] <= xEnd and yStart <= pos[1] <= yEnd:
                ans.append((x, y))
                maxY = max(maxY, currMaxY)
                break

        pos = [0,0]
print(ans)
print(maxY)
print(len(ans))
# for line in arr:
#     print(line)
