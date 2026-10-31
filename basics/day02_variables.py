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

#TASK 1
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


#calculator using operators
num1 = 50
num2 = 40

#ARithmetic operations
sum = num1 + num2
difference = num1 - num2
product = num1*num2
division = num1/num2
modulus = num1%num2
floor_division = num1//num2
exponentiation = num1**num2

print(sum)
print(difference)
print(product)
print(division)
print(modulus)
print(floor_division)
print(exponentiation)

#checking if a number is even or odd
number = 7
if number %2 == 0:
    print("the number is even")
else:
    print("the number is odd")

#TASK 3 
x = 2
y = 5

print(x>y)
print(x==y)
print(x<y)
print(x!=y)

##TASK 4 eligiblity check
age = 22
qualification = True
if 18<= age and qualification:
    print("eligible")

#TASK 5 discount calculation
price = 1000
discount = 10/100
final_price = price - (price * discount)
print(final_price)