# even or odd checking
num1 = int(input("enter the number ="))
if num1%2 == 0 :
    print("even")
else:
    print("odd")


num = int(input("enter a number ="))
if num>=1:
    print("The number is positive")
elif num<=-1:
    print("The number is negitive")
else:
    print("The number is zero")


n1 = int(input("enter the number:"))
n2 = int(input("enter the number:"))
if n1>n2:
    print("largest number is:", n1)
elif n2>n1:
    print("largest number is:", n2)
else:
    print("both numbers are equal:")


n1 = int(input("enter the number:"))
n2 = int(input("enter the number:"))
n3 = int(input("enter the number:"))
if n1>n2 and n1>n3:
    print("largest number is:", n1)
elif n2>n1 and n2>n3:
    print("largest number is:", n2)
else:
    print("largest number is:", n3)
 
 #          (or)
 # print("largest number is:", max(n1, n2, n3))


# leap year

year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
   print("not leap year")

