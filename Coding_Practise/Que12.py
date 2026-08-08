word="programming"
for i in word:
    count = 0
    for j in word:
        if i==j:
            count+=1
    print(f"{i}: ",count)

# or 

wording="PROGRAMMING"
char_count={}

for char in wording:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print(char_count)

for char,count in char_count.items():
    print(char + ':',count)