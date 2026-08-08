str="education"
count=0
for i in str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print(count)

# Or 
word="education"
count2=0
for i in word:
    if i in "aeiou":
        count2+=1
print(count2)