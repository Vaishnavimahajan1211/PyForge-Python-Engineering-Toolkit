#FOR loop

for i in range (1,6):
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  

for x in "banana":
    print(x)    



fruits = ["apple", "banana", "cherry"]    
for x in fruits:
    if x == "banana":
        continue
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)  

for x in range(6):
  print(x)    

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