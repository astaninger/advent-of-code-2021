#!/usr/bin/env python

import sys, itertools, collections, heapq

arr = []
for line in sys.stdin:
    arr.append(list(map(int, list(line.strip()))))

# with open("input.txt") as file:
#     inp = file.read().strip()
ans = 0
sinks = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        count = 0
        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i,j-1]]:
            if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                if arr[i][j] < arr[x][y]:
                    count += 1
            else:
                count += 1

        if count == 4:
            ans += 1 + arr[i][j]
            sinks.append([i, j])

print(ans)

ans = []
visited = set()
stack = []
for i, j in sinks:
    count = 0
    stack.append([i, j])
    while stack:
        i, j = stack.pop()
        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i,j-1]]:
            if (x, y) not in visited and 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] != 9:
                count += 1
                visited.add((x, y))
                stack.append([x, y])
    ans.append(count)
ans.sort()
ans1 = 1
for c in ans[-3:]:
    ans1 *= c
print(ans1)