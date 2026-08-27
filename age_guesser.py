import random

def main():
	print("Hello. I am going to guess your age.")
	guess_name()

def guess_name():
	
	name = input("What is your name? ")
	guess_right = False
	while not guess_right:
		
		age = random.randint(15, 40)
		guess = input("Is your age " + str(age) + "? y/n" )
		if guess == "y":
			print(name + " is " + str(age) + " years old.")
			guess_right = True
		elif guess == "n":
			print("Rats.")
	return

main()