# swapping with temp variable
a = 10
b = 20
print("before swapping:")
print("a=", a)
print("b=", b)
temp = a
a = b
b = temp
print("after swapping:")
print("a=",a)
print("b=",b)
# swapping without temp variable
x = 30
y = 40
print("before swapping:")
print("x=", x)
print("y=", y)
x = x+y
y = x-y
x = x-y
print("after swapping:")
print("x=", x)
print("y=", y)
