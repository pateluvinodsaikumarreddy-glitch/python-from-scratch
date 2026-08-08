# Fibonacci series 
first=0
second=1
print(first,second,end=" ")
for _ in range(8):
    sum=first+second
    print(sum,end=" ")
    first,second=second,sum
    """
    Or u can write 
    first=second
    second=sum
    """
print()