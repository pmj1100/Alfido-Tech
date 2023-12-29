import random
lower='abcdefghijklmnopqrstuvwxyz'
upper=lower.upper()
symbols='!@#$%^&*()_=+-[]}{;:/?><.,'
numbers='1234567890'
all=lower+upper+symbols+numbers
length=8
password=''
for _ in range(length):
    password=''.join({password,random.choice(all)})
print("generated password=",password)
