#FOR loop

for i in range (1,6):
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  

for x in "banana":
    print(x)    


#while loop  
count = 1
while count <= 5:
    print(count)
    count += 1

fruits = ["apple", "banana", "cherry"]    
for x in fruits:
    if x == "banana":
        continue
    print(x)