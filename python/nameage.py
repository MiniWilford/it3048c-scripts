import time

# Time Variables
start_time = time.time()
programAge = int(time.time() - start_time)


# Main Logic

print("What is your name?")

myName = input()

print("Hello, " + myName + ". That is a good name. How old are you?")

myAge = int(input())

print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))

print("I wish I was %i years old" %(myAge*2))

# Sleep functionality
time.sleep(3)
print("I'm tired. I go sleep sleep now.")

#
