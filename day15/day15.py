#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(line.strip())

grid = []
for line in arr:
    grid.append(list(map(int, line)))

def index(x):
    x = x % 9
    if x == 0:
        return 9
    else:
        return x
        

visited = [[False for _ in range(len(grid[0])*5)] for _ in range(len(grid)*5)]
dist = [[float('inf') for _ in range(len(grid[0])*5)] for _ in range(len(grid)*5)]
pqueue = [(0, 0)]
dist[0][0] = grid[0][0]
while pqueue:
    x, y = heappop(pqueue)
    for i, j in [[x+1, y], [x-1, y], [x, y+1], [x,y-1]]:
        if 0 <= i < len(grid)*5 and 0 <= j < len(grid[0])*5:
            iDiv, iMod = divmod(i, len(grid))
            jDiv, jMod = divmod(j, len(grid[0]))
            alt = dist[x][y] + (index(grid[iMod][jMod] + iDiv + jDiv) )
            if alt < dist[i][j]:
                dist[i][j] = alt
                heappush(pqueue, (i, j))
# for line in dist:
#     print(line)
print(dist[-1][-1]-1)


