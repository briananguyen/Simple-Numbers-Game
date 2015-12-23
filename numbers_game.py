"""System picks a random number between 1-100, user guesses and system responds with yes or no"""

import random
import os
import time


def guess():
	numbers = random.sample(xrange(1, 101), 100)
	random_num = random.choice(numbers)

	while True: 
		choice = int(raw_input("I've chosen a number between 1 and 100, can you guess what it is?: "))

		if choice > random_num:
			print("Incorrect, too high :(")
			quit = raw_input("Should I release the answer (quit the game)? y/n: ")
			if quit == "y":
				print(random_num)
				print("Thanks for playing!")
				exit()
			else:
				choice

		if choice < random_num:
			print("Incorrect, too low :(")
			quit = raw_input("Should I release the answer (quit the game)? y/n: ")
			if quit == "y":
				print(random_num)
				print("Thanks for playing!")
				exit()
			else:
				choice

		if choice == random_num:
			print("Yay! You've guessed correctly!")
			time.sleep(0.5)
			repeat()

def repeat():
	while True:
		decision = raw_input("Would you like to play again? y/n: ")

		if decision == "y":
			guess()
		elif decision == "n":
			print("Thanks for playing!")
			exit()
		else: 
			print("Invalid input")
			repeat()

guess()