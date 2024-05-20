# lambda or Annynomous function 

# syntax : lambda arg: Expression

# (multiline comment ctrl + /)

num = [8,2,1,3,5,6]
even = []
odd = []
for item in num:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

print(f"even ={even}")
print(f"even ={odd}")