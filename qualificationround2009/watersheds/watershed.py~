# Given an elevation map (a 2-dimensional array of altitudes), label the map such that locations in the same drainage basin have the same label, subject to the following rules.

#    From each cell, water flows down to at most one of its 4 neighboring cells.
#    For each cell, if none of its 4 neighboring cells has a lower altitude than the current cell's, then the water does not flow, and the current cell is called a sink.
#    Otherwise, water flows from the current cell to the neighbor with the lowest altitude.
#    In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.

#Every cell that drains directly or indirectly to the same sink is part of the same drainage basin. Each basin is labeled by a unique lower-case letter, in such a way that, when the rows of the map are concatenated from top to bottom, the resulting string is lexicographically smallest. (In particular, the basin of the most North-Western cell is always labeled 'a'.) 


v = [line.strip().split() for line in open('test.txt')]
print v


for i in range(0, int(v.pop(0)[0])):
  print ("Case #" + str(i+1) + ":\n")
