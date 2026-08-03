n=9
# upper part
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("X" * (2*i-1))
# Lower part 
for i in range(n-1,0,-1):
    print(" "*(n-1),end="")
    print("X" * (2*i-1))