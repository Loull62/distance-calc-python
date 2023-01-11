# DISTANCE CALCULATOR BETWEEN TWO POINTS

import math

print("WELCOME TO THE DISTANCE CALCULATOR!")

# input

pointx1 = float(input("\nEnter x1 value: "))
pointy1 = float(input("Enter y1 value: "))
pointx2 = float(input("Enter x2 value: "))
pointy2 = float(input("Enter y2 value: "))

# process

result = math.sqrt((pointx2 - pointx1)**2 + (pointy2 - pointy1)**2)

# output

print("\nThe distance between the two points is " + str(result) + ".")