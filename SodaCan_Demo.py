# Davis Arita
# 11/14/22
# CS 131 Lecture 12A lab 1
# implmenting classes

from IC1_SodaCan import SodaCan

can1 = SodaCan(height=float(input("Enter the height: "))
               , radius=float(input("Enter the radius: ")))

print("The surface area of can 1(h = %d, r = %d) is: %.2f" % (can1.getHeight()
                                                              , can1.getRadius(),
                                                              can1.getSurfaceArea()))
