import random

def main():
    print("Hello. I am going to guess your age.")
    guess_name()

def guess_name():

    name = input("What is your name? ")
    guess_right = False
    age_old = 40
    age_young = 15
    while not guess_right:

        age = random.randint(age_young, age_old)
        guess = input("Is your age " + str(age) + "? y/n" )
        if guess == "y":
            print(name + " is " + str(age) + " years old.")
            guess_right = True
        elif guess == "n":
            print("Rats.")
            ques = input("older or younger?")

            if ques == "older":
                age_young = age+1
            
            if ques == "younger":
                age_old = age-1
    
    return

main()