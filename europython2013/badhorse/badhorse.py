from math import asin, degrees

l = [line.strip().split() for line in open('small1.in')]

def solve(l):
    groups = [[],[]]
    m = int(l.pop(0)[0])
    for i in range(0, m):
        print groups
        if (l[i][0] not in groups[0] and l[i][1] not in groups[0]):
            groups[0].append(l[i][0])
            if (l[i][1] not in groups[1]):
                groups[1].append(l[i][1])
        elif (l[i][0] not in groups[1] and l[i][1] not in groups[1]):
            groups[1].append(l[i][0])
            if (l[i][1] not in groups[0]):
                groups[0].append(l[i][1])
        
        #elif not in either for both        
        elif (l[i][0] not in groups[0] and l[i][0] not in groups[1] and l[i][1] not in groups[0] and l[i][1] not in groups[1]):
            groups[0].append(l[i][0])
            groups[1].append(l[i][1])
        else:
            for i in range(0, m):
                l.pop(0)
            return "No"
    for i in range(0, m):
        l.pop(0)
    return "Yes"

length = int(l.pop(0)[0])
for i in range(0, 2):
    print "Case #" + str(i+1) + ": " + str(solve(l))
