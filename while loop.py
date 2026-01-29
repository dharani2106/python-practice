# while loop problems

lst = [12,13,14,15,16]
i  = 0
while i>-5:
    print(lst[i])
    i=i-1

# printing numbers 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# printing numbers 10 to 1

i = 10
while i >= 1:
    print(i)
    i -= 1

# sum of digits
n = 5
sum = 0
i = 0
while i < n:
    sum += i
    i += 1
print("sum =", sum)

# while loop with user input
n = int(input("enter the number ="))
while n >0:
    print(n)
    n -=  1

# reverse number

num = int(input("enter the number:"))
reverse = 0
while num >0:
    digit = num%10
    reverse = reverse*10+digit
    num = num //10
print("reverse:", reverse)


#count the num of digits in a num

num = int(input("enter the number:"))
count = 0
while num >0:
    count += 1
    num = num // 10
print("number of digits =", count)


# even numbers b/w 1 and 20
i = 1
while i <= 20:
    if i%2 == 0:
       print(i)
    i += 1
i = 1
while i <= 20:
    if i%2 == 0:
       print(i)
    i += 1
