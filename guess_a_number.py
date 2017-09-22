
        
import random
import math
# config
low = 1
high = 100
limit = math.ceil(math.log(100,2))

# helper functions
def show_start_screen():
    print("**************************")
    print("**** Guess a Number ! ****")
    print("**************************")

def show_credits():
    print("********************This dope game was created by***************")
    print("***************************** THE AMAZING ELI!!!!*********************")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")
            print()
            

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". you have" +  str (limit) + " tries.")
    print()


    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print()
    elif guess > rand:
        print("You guessed too high.")
        print()

def show_result(guess, rand):
    if guess == rand:
        print("You win! Your so good at this now move out of your moms basement and go get a life.")
        print()

    else:
        print("you are so stupid! you should be deleted out of space and time. The number was " + str(rand) + ".")
        print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()
        

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("really?! do you know what a y or an n is.. clearly not.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
