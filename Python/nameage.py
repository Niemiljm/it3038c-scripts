import time

start_time = time.time()

print('What is your name?')
myName = input()

#while loop example
while myName != "Joe":
    if myName == 'your name':
        print("Not funny, dad. What's your real name?")
        myName=input()
    else:
        print('You are not authorized to use this program')
        myName=input()

print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

#Sample If Statements
if myAge < 13:
    print("Learning young, that's pretty cool I guess")
elif myAge == 13:
    print("You're a teenager now... Time for high school?")
elif myAge > 13 and myAge < 30:
    print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:
    print("Now you're an adult, nerd")
else:
    print(".... what were the dinosaurs like?")

time.sleep(1)
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old" % (myAge, programAge))    
print("I wish I was %s years old" % (myAge * 2))

time.sleep(3)
print("I'm tired. I sleep now")