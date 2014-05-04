from interface import Interface
from triangle import Triangle

sides, angles = Interface().run()

tri = Triangle(sides, angles)

tri.compute()

print(tri)
