nums=[10,20,4,55,99]
largest=0
second_largest=0
for num in nums:
    if num > largest:
        second_largest = largest
        largest=num
    elif num > second_largest and num!=largest:
        second_largest=num
print("Second largest num is: ",second_largest)




nums=[10,20,15]
largest=0
second_largest=0
for num in nums:
    if num > largest:
        second_largest = largest
        largest=num
    elif num > second_largest and num!=largest:
        second_largest=num
print("Second largest num is: ",second_largest)