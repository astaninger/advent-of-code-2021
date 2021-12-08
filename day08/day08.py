#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

# with open("input.txt") as file:
#     inp = file.read().strip()
ans = 0
for line in arr:
    a, b = line.split(' | ')
    for s in b.split():
        if len(s) in [2, 3, 4, 7]:
            ans += 1
print(ans)
ans = []
nums = {0: set('abcefg'), 1:set('cf'), 2:set('acdeg'), 3:set('acdfg'), 4:set('bcdf'), 5:set('abdfg'), 6:set('abdefg'), 7:set('acf'), 8:set('abcdefg'), 9:set('abcdfg')}
for line in arr:
    a, b = line.split(' | ')
    d = {'a': '', 'b': '', 'c': '', 'd':'', 'e':'', 'f':'', 'g':''}
    buckets = collections.defaultdict(list)
    counts = collections.Counter()
    for s in a.split():
        buckets[len(s)].append(s)
        for c in s:
            counts[c] += 1
    one = set(buckets[2][0])
    two = set(buckets[3][0])
    # print(buckets)
    d[next(iter(two-one))] = 'a'
    for k, v in counts.items():
        if v == 4:
            d[k] = 'e'
        elif v == 6:
            d[k] = 'b'
        elif v== 9:
            d[k] = 'f'
            one.remove(k)
            d[next(iter(one))] = 'c'
    for c in buckets[4][0]:
        if d[c] == '':
            d[c] ='d'
    for k, v in d.items():
        if v == '':
            d[k] = 'g'
    total = 0
    for s in b.split():
        curr = set()
        for c in s:
            curr.add(d[c])
        for k, v in nums.items():
            if curr == v:
                total = (total*10) + k
    ans.append(total)
    total = 0
print(sum(ans))
