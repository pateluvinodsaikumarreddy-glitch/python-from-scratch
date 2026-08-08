"""
Print Even number between 1 to 10 
Expected O/p: 2,4,6,8,10
Hint:num%2==0 
"""
for i in range(1,11):
    if(i%2==0):
        print("Even Number",i, end=" ")
        print()
    else:
        print("Odd Numbers",i)
