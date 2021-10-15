# Number 4
a = float(input("Enter the number of packages purchased: "))
b = a * 99
c = b * (10/100)
d = b * (20/100)
e = b * (30/100)
f = b + (40/100)

g = b - c
h = b - d
i = b - e
j = b - f

if a >= 10 and a <= 19:
    print("Discount Amount @ 10%: $ ", format(c, '.2f'))
    print("Total Amount: $", format(g,'.2f') )
elif a >= 20 and a <= 49:
    print("Discount Amount @ 20%: $ ", format(d,'.2f'))
    print("Total Amount: $", format(h,'.2f') )
elif a >= 50 and a <= 99:
    print("Discount Amount @ 30%: $ ", format(e,'.2f'))
    print ("Total Amount: $", format(i,'.2f'))
elif a >= 100:
    print("Discount Amount @ 40%: $ ", format(f,'.2f'))
    print("Total Amount: $", format(j,'.2f'))
elif a < 0:
    print("No quantity below 0")
else:
    print("Discount Amount @ 0%: $ 0.00")
    print("Total Amount: $", format(b,'.2f'))

#input the quantity
#the program will decide which range it is
#print discount amount
#print total amount