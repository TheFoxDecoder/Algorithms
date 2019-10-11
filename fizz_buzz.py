'''
Algorithm:-  Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. 
                In other words, if a number is divisible by 3, it is substituted with fizz; 
                if a number is divisible by 5, it is substituted with buzz. 
                If a number is simultaneously a multiple of 3 AND 5, the number is replaced with "fizz buzz." 
   '''             
import array as arr


#3 is fizz 5 is buzz
number = [] # Creating empty list
n = int(input("Enter the number of Elements")) # inputting number of elements

#Using for loop getting use inputs
for i in range(0, n): 
    elements = int(input()) 
  
    number.append(elements) # adding the element 


#Calculation
for num in number:
    if (num % 3 == 0):
        print("%d Fizz"%num)
    elif (num %5 == 0):
        print("%d Buzz"%num)
    else :
        print(num)    


