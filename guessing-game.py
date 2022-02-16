import random
from random import randint

print ("Welcome to the number guessing game!")
random.seed(input("Enter random seed: "))
play = "yes"

while play == "yes":
    rand_number = randint(1, 99)
    trials = 0
    for trials in range(1, 101, 1):
        guess = int(input ("\nPlease enter a guess: "))
        if guess > rand_number:
            print ("Lower")
            trials += 1
        elif guess < rand_number:
            print ("Higher")
            trials +=1
        else:
            print ("Congratulations. You guessed it!\n" + "It took you {} guesses.".format(trials))
            play = input("\nWould you like to play again (yes/no)? ")
            if play == "no":
                print ("Thank you. Goodbye.")
            elif play != "yes":
                print ("That is not a valid input")
            break
            

print ("David was here")