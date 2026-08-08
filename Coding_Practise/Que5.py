# Reverse of a string "Python" to "nohtyP"
str="Python"
for i in range(len(str)-1,-1,-1):
    print(str[i],end=" ")
print()

# OR using Slicing

STR="Vinod"
new_str= STR[::-1]
print(new_str)

# Or use for loop and variable
STR2="Sai"
ReversedStr=""
for char in STR2:
    ReversedStr=char+ReversedStr
print(ReversedStr)
