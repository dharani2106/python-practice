# loops with conditions 

for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i)

for i in range(1,51):
    if i == 30:
        break
    print(i)

for i in range(1,51):
    if i%3==0 and i%7==0:
        print(i)

#prime numbers

for num in range(2,100):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
