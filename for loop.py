for i in range(1,11):
     print(i)

# even numbers
for i in range(2,51,2):
    print(i)

 #    (or)

for i in range(1,51):
    if i % 2 == 0:
       print(i)

# odd numbers

for i in range(1,50):
    if i % 2 != 0:
       print(i)
 
#        (or)

for i in range(1,50,2):
     print(i)


# printing multiplication table

num = int(input("enter the number:"))
for i in range(1,11):
    print(num ,"x",i, "=",num*i) 

# sum of first n natural numbers
sum = 0
for i in range(1,10):
    sum += i
print(sum)

# counting numbers 

count = 0
for i in range(1,101):
    if i % 3 == 0:
       count += 1
print("count:", count)

# using for loop to print same msg multiple times

for i in range(7):
    print("Sorry")

# using for loop with string

name = "Dharani"
for ch in name:
    print(ch)

# using for loop with list

lst = [23,45,76,87,34]
for i in lst:
    print(i)

# for loop with condition

for i in range(1,50):
    if i % 2 == 0:
       print(i)

# for loop with break condition

for i in range(1,12):
    if i == 8:
        break
    print(i)

# for loop with continue condition

for i in range(5,12):
    if i == 9:
        continue
    print(i)
