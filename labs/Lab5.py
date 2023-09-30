import random

# Introduction
print("Hello, guess a number between 0 and 10")		

def shouldContinue(resp):
	try:
		if resp == "yes" or resp == "y":
			print("\nContinuing...\n") 
			return True 
		else:
			print("\nGoodbye!")
			return False
	except:
		print("\nThe answer you given is invalid. Presuming termination...")
		return False

# Guess The Number Program
running = True
rand_num = int(random.random() * 10)

while running:
	# Generate a random integer between 0 and 10
	# Get user input and convert to integer
	resp = int(input("\nEnter a number: "))
	if(resp == rand_num):
		print("\nYou guessed the number! Correct!")
		# Ask user to continue
		print("\nDo you wish to continue? Yes or no?")
		answer = str(input()).lower() # Does not work on Python 2.7
		running = shouldContinue(answer) # Return True or False
		if running == True:
			rand_num = int(random.random() * 10)
	elif(resp < rand_num):
		print("\nThe number is higher.")
	elif(resp > rand_num):
		print("\nThe number is lower.")
	else:
		print("\nThat is not a number, try again.\n")
	
	
