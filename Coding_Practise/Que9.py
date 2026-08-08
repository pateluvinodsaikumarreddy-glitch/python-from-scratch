num=7
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not a prime number ")
        break
else:
     print(f"{num} is a prime number")
    
# or

num2=11
is_prime=True
for i in range(2, int(num2 ** 0.5)+1):
    if num2%i==0:
        is_prime = False
        break

if is_prime and num2>1:
    print(num2, "is a prime number")
else:
    print(num2, "is not a prime number")