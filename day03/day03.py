from collections import defaultdict
with open("/home/alex/Projects/advent-of-code-2021/day03/day03.in") as f:
    input = f.read()
A = input.split("\n")[:-1]
ans = 0
counts = defaultdict(dict)
for b in A:
    for i, d in enumerate(b):
        if d in counts[i]:
            counts[i][d] += 1
        else:
            counts[i][d] = 1
g, e = '', ''
for i in range(len(A[0])):
    if counts[i]['1'] > counts[i]['0']:
        g += '1'
        e += '0'
    else:
        e += '1'
        g += '0'
print(int(g, 2)* int(e, 2))

lastmaxes = list(A)
lastmins = list(A)
for i in range(len(A[0])):
    counts = defaultdict(int)
    _maxes = []
    _mins = []
    for b in lastmaxes:
        counts[b[i]] += 1
    take0 = True if counts['0'] > counts['1'] else False
    if len(lastmaxes) > 1:
        for b in lastmaxes:
            if take0 and b[i] == '0':
                _maxes.append(b)
            elif not take0 and b[i] == '1':
                _maxes.append(b)
    for b in lastmins:
        counts[b[i]] += 1   
    if len(lastmins) > 1:
        take0 = True if counts['0'] <= counts['1'] else False
        for b in lastmins:
            if take0 and b[i] == '0':
                _mins.append(b)
            elif not take0 and b[i] == '1':
                _mins.append(b)
    lastmins = _mins if len(lastmins) > 1 else lastmins
    lastmaxes = _maxes if len(lastmaxes) > 1 else lastmaxes
print(int(lastmins[0],2)* int(lastmaxes[0], 2))  