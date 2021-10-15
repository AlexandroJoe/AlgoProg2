# number 2

a = eval(input("Enter length of edge1: "))
b = eval(input("Enter length of edge2: "))
c = eval(input("Enter length of edge3: "))

perimeter = a + b + c

if a + b > c and a + c > b and b + c > a:
    print ("The perimeter is ", perimeter)
else:
    print ("Perimeter cannot be caluclate : input is invalid")

#input 3 lengths
#if the 3 lengths meet the condition 
#perimeter formula will be executed
# if the 3 lengths don't meet the requirement the input is invalid