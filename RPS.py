# Name
# Rock Paper Scissors
# add a comment
# Welcome message
#VARIABLES
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]


# Print the message
print("Welcome to Rock Paper Scissors ")
# prompt for player name
pName = input("What is your name? ")


# Game Loop

# Final Score
def printScore():
# Write message
	print("the score is: ")
# Write player score
	print(pName + ": " + str(pScore))
# write compute score
	print("Computer: " + str(cSore))
# write how many ties
	print("Ties: " + str(ties))

# Game Loop
# make a forever loop
while True:
	# Print current score
	printScore()
	#prompt for a choice (r(rock), p (paper), q (quit))
	pChoice = input("Enter r (rock), p (paper), s (scissors) or q (to quit): ")
	#compare for player entering q
	if cChoice == "q":
		break	
	# get computers choice(random)
	cCoice = random.choice(computerChoices)
	#compare for player entering r
	if pChoice == "r":
		print(pName + "(picked rock")
		
		# if computer is r
		if cChoice == "r":
			print("Computer chose rock")
			print(" This is a tie")
			ties = ties + 1
		# if computer is p
	elif cChoice == "p":
		print("Computer chose Paper")
		print("Paper covers rock")
		cScore = cScore +1
		# if computer is s
		elif:
		print("Computer picked Scissors")
		print(" Rock Breaks Scissors")
		cScore = pScore + 1
	# compare for player entering p
	elif pChoice == "p":
	print(pName + "Picked Paper")
	print("Computer chose rock")
	print(" Paper covers rock")
	# compare for player entering s
	elif pChoice == "s":
	print(pName + "Picked Scissors")
	
	# deal with player entering anything else