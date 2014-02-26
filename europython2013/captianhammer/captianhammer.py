from math import asin, degrees

l = [line.strip().split() for line in open('small.in')]

def solve(l):
    stuff = l.pop(0)
    V = float(stuff[0])
    D = float(stuff[1])
    tmp = (D * 9.8)/V**2.0
    if tmp > 1.0:
        tmp = 1.0
    if tmp < -1.0:
        tmp = -1.0
    return degrees(asin(tmp))/2.0


length = int(l.pop(0)[0])
for i in range(0, length):
    print "Case #" + str(i+1) + ": " + str(solve(l))
