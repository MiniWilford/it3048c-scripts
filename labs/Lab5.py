import random
import sys

# Python Version
python_version = int(sys.version[0])
print(python_version)

# Introduction
print("\n\nHello, guess a number between 0 and 10")		

def shouldContinue(resp):
	if resp == "yes" or resp == "y":
		print("\nContinuing...\n") 
		return True 
	else:
		print("\nGoodbye!")
		return False

# Guess The Number Program
running = True
rand_num = int(random.random() * 10)

while running:
	# Generate a random integer between 0 and 10
	# Get user input and convert to integer
	try:	
		resp = int(input("\nEnter a number: "))
	except:
		print("\nYou did not enter an integer...")
	try:
		if(resp == rand_num):
			print("\nYou guessed the number! Correct!")
			# Ask user to continue (does not work if Python 2.X.X and below)
			if(python_version > 2):
				answer = str(input("\nDo you wish to continue? Yes or no: ")).lower()
				running = shouldContinue(answer)
			elif(python_version < 3):
				print("Do you wish to continue? y / n: ")
				answer_python_two = raw_input() #Raw_input is necessary in Python2, input is Python3
				running = shouldContinue(answer_python_two)			
			else:
				print("Invalid Python Version")
				break;
			# Determine if to keep running
			if running == True:
				rand_num = int(random.random() * 10)
		elif(resp < rand_num):
			print("\nThe number is higher.")
		elif(resp > rand_num):
			print("\nThe number is lower.")
		else:
			print("You broke something")
	except:
		print("Invalid input, try again")
	
