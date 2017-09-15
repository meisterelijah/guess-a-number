import random
#comfig

low = 1
high = 100
limit = 10

            

#helper functions
def get_guess():
    while True:
        guess = input ("guess a number.")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print ("you must enter a number.")

#start game
rand = random.randint(low, high)
print("I'm thinking of a number from "  + str(low) +  " to " + str(high) + ".");

guess = -1
tries = 0

#play game

while guess != rand and tries < limit:
    guess = get_guess
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

    tries += 1
        
#end game

if guess == rand:
    print ("your are so good at this now go get a life!!")
    
else:
    print("Game over, you just need to jumb off a building if you didn't get that the number was" + str(rand) + ".")
