import math
fps = 23.97
# goes from {0, 1, 2, ... fps-1}

frames = 19

proportion = frames/float(fps)

print int(math.floor(proportion*1000))
print 792-58417