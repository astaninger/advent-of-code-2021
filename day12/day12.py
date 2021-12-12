#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

graph = defaultdict(list)
for line in stdin:
    u, v = line.strip().split('-')
    graph[u].append(v)
    graph[v].append(u)

stack = [('start', set(['start']))]
paths = 0
while stack:
    curr, visited = stack.pop()
    if curr == 'end':
        paths+=1
        continue
    if curr.lower() == curr:
        visited.add(curr)
    for nei in graph[curr]:
        if nei not in visited:
            stack.append((nei, set(visited)))

print(paths)

stack = [('start', set(['start']), False)]
paths = 0
while stack:
    curr, visited, used = stack.pop()
    if curr == 'end':
        paths+=1
        continue
    if curr.lower() == curr:
        visited.add(curr)
    for nei in graph[curr]:
        if nei not in visited:
            stack.append((nei, set(visited), used))
        elif nei != 'start' and nei != 'end' and nei in visited and not used:
            stack.append((nei, set(visited), True))

print(paths)