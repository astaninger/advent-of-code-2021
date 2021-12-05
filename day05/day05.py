#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

board = [[0 for _ in range(1000)] for _ in range(1000)]
for line in arr:
    start, end = line.split(' -> ')
    startX, startY = start.split(',')
    endX, endY = end.split(',')
    startX = int(startX)
    startY = int(startY)
    endX = int(endX)
    endY = int(endY)
    # if startY != endY and startX != endX: continue
    diffI, diffJ = -1 if startX > endX else (0 if startX == endX else 1), -1 if startY > endY else (0 if startY == endY else 1)
    i,j = startX, startY
    while min(startX, endX) <= i <= max(endX, startX) and min(startY, endY) <= j <= max(endY, startY):
        board[i][j] += 1
        i += diffI
        j += diffJ
    
ans = 0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] > 1:
            ans += 1

print(ans)
    

