# # Explicit type casting 
a=10
b="10"
print(type(b))

b_new=int(b)
print(type(b_new))

a_new=str(a)
print(type(a_new))


#implicit typecasting


num = "100"

print(type(num))      # Before conversion

num = int(num)

print(type(num))      # After conversion