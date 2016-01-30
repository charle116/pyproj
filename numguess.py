#!/usr/bin/env python3

# re: https://www.youtube.com/watch?v=pofWfJc3Zog&index=22&list=WL
# example of: print integer, int compare, if, elif, else, random, randint

""" This has the user guess a number between 1 and 100, and gives hints """

# set random integer
import random
randomNumber = random.randint(1,100)

print ("Here you go cheater!: %d" % randomNumber )
print ("Guess a number between 1 and 100")

#randomNumber = 32, use for debugging only
found = False 

while not found:
	userGuess = int(input("Your guess: "))
	if userGuess == randomNumber:
		print ("You guessed it!")
		found = True
	elif userGuess > randomNumber:
		print ("Guess lower!")
	else:
		print ("Guess Higher!")

