#Arithmetic operators
a = 10
b = 3

print(a+b)
print (a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#comparison operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators
age = 22
has_id = True
print (age > 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

#Assignment operators
x = 5
x += 3
print(x)

#Membership operators
#in
#not in 
skills = ["python", "sql", "azure"]
print ("python" in skills)
print("java" in skills)

#identify operators
#is
#is not

a = [1, 2, 3]
b = a
c= [1, 2, 3]
print (a is b)
print (a is c)
print (a==b)
print(a is not c)