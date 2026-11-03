   

#while loop  
count = 1 
while count <= 8:
    print("Hello")
    count += 1

print("count is", count)

i = 1
while i <=5:
   print ("oh!" , i)
   i += 1 

i = 10
while i >=0:
    print(i)   
    i -=  1
print("loop is over")    
 

#print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i +=1

#print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


#print the multiplication table of a number n
n = 3
while n<= 30:
    print(n)
    n += 3

#print the element of list [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


heros = ["Ironman", "Thor", "Hulk", "Captain America", "Black Widow"]
idx = 0 
while idx < len(heros):
    print(heros[idx])
    idx +=1

#search for number x in this tuple using loops:
kumkum = (1, 4 ,9, 16, 25, 36, 49, 64, 81, 100)

x = 36 
i = 0 #initialization
while i < len(kumkum):
    if(kumkum[i] == x):
      print(i)
    i += 1 

#while loop use karke 1 se 10 tak numbers ka total calculate karo.
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Total:", total)


#break statement

i = 0
while i < 20:
    print(i)
    if(i == 16):
        break
    i += 1
print("loop is over")

a = 4 
b = 4
if a != b :
    if a % b == 0:
        a = a*2 + 1
        b = b ** 2 + 2
    else :
        b = b ** 2
        a = b *2
print(a +b)

#continue statement
i = 0 
while i<=5:
    if(i == 3):
        i += 1
        continue  #skip
    print(i)
    i += 1

#print even number between 1 to 20 using while 
i = 0 
while i <= 20:
          print(i)
          i += 2

  # method nuber two
i = 0
while i <= 20:
      if i % 2 == 0:
          print(i)
      i += 1



       
