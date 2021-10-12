# number 1
import math

m = float(input("Enter the mass of the cart (in kg): "))
f = float((input("Enter the force to push the cart (in N): ")))
g = 9.8

degree = f/(m*g)

A = math.degrees(degree)
print ("The angle of the ramp is", "{:,.2f}".format(A), "degrees")