# import complex math module
import cmath
a=float(input("Enter the 1st no:"))
b=float(input("Enter the 2nd no:"))
c=float(input("Enter the 3rd no:"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

