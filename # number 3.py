# number 3
a = eval(input("Enter the temperature in Fahrenheit: "))

x = 0
while x < 1:
    if -58 < a < 41:
        b = eval(input("Please enter the wind speed in miles per hour"))
        break
    else:
        print("The temperature must be between -58F and 41F: ")
        a = eval(input("Please re-enter the temperature in Fahrenheit: "))

while x < 1:
    if b >= 2 :
        c = 35.74 + (0.6215 * a) - 35.75 * (b ** 0.16) + 0.4275 * a * (b ** 0.16)
        print("The wind chill index is", format(c,'.3f'))
        break
    else:
       print("Speed must be greater than or equal to 2")
       b = eval(input("Please re-enter the wind speed miles per hour : "))

#input the temperature
#if the temperature is beyond the range, re-input
#enter the wind speed if the temperature is in the range
#If the wind speed beyond the range, re-input
#Execute the formula if the wind speed is in the range
#Print the wind chill index