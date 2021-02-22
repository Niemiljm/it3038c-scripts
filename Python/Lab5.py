# Lab 5: Take a number input and calculate how many prime numbers come between it and 0 
# I decided to take it a step further and make both range numbers as imputs, then count them using the counting variable!

print('What is the lower range number?')
lowerRange = int(input())

print('What is the upper range number?')
upperRange = int(input())
counting = 0

print("The prime numbers between", lowerRange, "and", upperRange, "are as follows:")

for number in range(lowerRange, upperRange + 1):
   if number > 1:
       for i in range(2, number):    
           if (number % i) == 0:
               break
       else:
           print(number)
           counting+=1   
      
print("The total number of prime numbers within this range is:", counting)