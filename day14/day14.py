#!/usr/bin/env python

from sys import *
from collections import *
from itertools import *
from heapq import *

arr = []
for line in stdin:
    arr.append(line.strip())

curr = list(arr[0])
graph = {}
for line in arr[2:]:
    u, v = line.split(' -> ')
    graph[u] = [u[0]+v, v+u[1], v]
counts = Counter()
for i in range(len(curr)-1):
    counts[curr[i] + curr[i+1]] += 1
    counts[curr[i+1]] -= 1
for _ in range(40):
    lastCounts = dict(counts)
    for pair in lastCounts.keys():
        if len(pair) == 1: continue
        a, b, c = graph[pair]
        counts[a] += lastCounts[pair]
        counts[b] += lastCounts[pair]
        counts[c] -= lastCounts[pair] 
        counts[pair] -= lastCounts[pair]

c = Counter()
for pair in counts.keys():
    if len(pair) == 2:
        c[pair[0]] += counts[pair]
        c[pair[1]] += counts[pair]
    else:
        c[pair] += counts[pair]
print(c)
print(max(c.values()) - min(c.values()))

