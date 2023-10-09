import time

# Time Variables
start_time = time.time()
programAge = int(time.time() - start_time)


# Main Logic

print("What is your name?")

myName = input()

# Control Logic
while myName != "AJ":
	if myName == "your name":
		print("Ha Ha, very funny. Seriously, who are you?")
		myName = input()
	else:
		print("That is not your name. Please, tell me your real name.")
		myName = input()

print("Hello, " + myName + ". That is a good name. How old are you?")

myAge = int(input())

print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))

print("I wish I was %i years old" %(myAge*2))

# Sleep functionality
time.sleep(3)
print("I'm tired. I go sleep sleep now.")

# If Logic
if myAge < 13:
	print("Learning young, that's good")
elif myAge == 13:
	print("You're a teenager now... that's cool, I guess")
elif myAge > 13 and myAge < 30:
	print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:
	print("Now you're adulting.")
else:
	print("...you've lived a long time?")



