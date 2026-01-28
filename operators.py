# Operators Practice Problems
n1 = 12
n2 = 14
add = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2
mod = n1%n2
floor_div = n1//n2
exp = n1**n2
print("add:",add)
print("sub:",sub)
print("mul:",mul)
print("div:",div)
print("mod:",mod)
print("floor_div:",floor_div)
print("exp:",exp)

num = int(input("enter the number:"))
if num>100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")

num = int(input("enter a number:"))
if num >= 10 and num <= 50:
    print("Number lies between 10 and 50:")
else:
    print("Number does not lies between 10 and 50:")

# using one variable and demonstrating assignment operators

x = 10
x += 12
x -= 16
x *= 23
x /= 2
print(x)

x = int(input("enter the number:"))
x += int(input("enter the number:"))
print("after +=",x)
x -= int(input("enter the number:"))
print("after -=",x) 
x *= int(input("enter the number:"))
print("after *=",x)
x /= int(input("enter the number:"))
print("after /=",x)
x %= int(input("enter the number:"))
print("after %=",x)


num = int(input("enter the number:"))
if num%3 == 0 and num%5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")


num = int(input("enter the number:"))
remainder = num % 7
print("remainder=",remainder)


