from random import randint, seed
from math import ceil, sqrt, log, floor

import delaunay as D

seed(4)
n = 40
xs = [randint(1, 98) for x in range(n)]
ys = [randint(1, 98) for x in range(n)]
zs = [0 for x in range(n)]

DT = D.Delaunay_Triangulation()
for x, y in zip(xs, ys):
    DT.AddPoint(D.Point(x, y))

XS, YS, TS = DT.export()

#print(xs)
#print(ys)

#print(XS)
#print()
#print(YS)
#print()
#print(TS)
#print()

"""
Creating and plotting unstructured triangular grids.
"""
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import math

# Creating a Triangulation without specifying the triangles results in the
# Delaunay triangulation of the points.

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(xs, ys)

# Plot the triangulation.
fig, ax = plt.subplots()
ax.margins(0.1)
ax.set_aspect('equal')
#ax.triplot(triang, 'b-')

#ax.triplot(tri.Triangulation(XS, YS, TS), 'r-')
'''for triangle in TS:
 t = D.Triangle(D.Point(XS[triangle[0]], YS[triangle[0]]), D.Point(XS[triangle[1]], YS[triangle[1]]), 
  D.Point(XS[triangle[2]], YS[triangle[2]]))
 p = t.CircumCentre()
 print(p)'''
eList = DT.GetVoronoiEdges()
for e in eList:
 if e[0].x > 0 and e[0].x < 100 and e[1].x > 0 and e[1].x < 100 and e[0].y > 0 and e[0].y < 100 and e[1].y > 0 and e[1].y < 100:
  plt.plot((e[0].x, e[1].x), (e[0].y, e[1].y), 'b')
#plt.plot((0,99),(0,99), 'b-')
#ax.triplot(lines.Line2D((0,99),(0,99)))
ax.set_title('triplot of Delaunay triangulation')

plt.show()




