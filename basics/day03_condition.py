#if statement
age = 22
if age >= 18 :
    print("you are not eligible to vote")
    
#if - else

temperature = 15

if temperature> 25:
    print("it is hot outside")
else:
    print("it is cold outside")    

#if - else - elif 

marks = 75

if marks>= 90:
    print("A Grade")
elif marks>= 75:
    print("B Grade")
elif marks>= 60:
    print("C Grade") 
elif marks>= 40:
    print("D Grade")       
else :
    print("Fail")    

#Nested if    
age = 22
has_id = False

if age>= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Entry not allowed")            

#short hand if else
marks = 35
result = "pass" if marks >= 40 else "fail"
print (result)    


#task 01 voting eligiblity
age = 17 
if age>= 18 :
    print ("you are eligible to vote")
else :
    print("you are not eligible to vote")    


#task 2 student grading system
marks = 85 


if marks>= 90:
    print("A Grade")
elif marks>= 75:
    print("B Grade")
elif marks>= 60:
    print("C Grade") 
elif marks>= 40:
    print("D Grade")       
else :
    print("Fail") 