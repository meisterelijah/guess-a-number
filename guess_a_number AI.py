import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("""  _______                                
(_______)                               
 _   ___ _   _ _____  ___  ___    _____ 
| | (_  | | | | ___ |/___)/___)  (____ |
| |___) | |_| | ____|___ |___ |  / ___ |
 \_____/|____/|_____|___/(___/   \_____|
                                        
 _______             _                    _______   _   _ 
(_______)           | |                  (_______) | | | |
 _     _ _   _ ____ | |__  _____  ____    _______  | | | |
| |   | | | | |    \|  _ \| ___ |/ ___)  |  ___  | | | |_|
| |   | | |_| | | | | |_) ) ____| |      | |   | |_| |_ _ 
|_|   |_|____/|_|_|_|____/|_____)_|      |_|   |_(_)_(_)_|
                                                           """)
  
def show_credits():
    print(""" _______  _       __________________ _______          
(  ____ \( \      \__   __/\__    _/(  ___  )|\     /|
| (    \/| (         ) (      )  (  | (   ) || )   ( |
| (__    | |         | |      |  |  | (___) || (___) |
|  __)   | |         | |      |  |  |  ___  ||  ___  |
| (      | |         | |      |  |  | (   ) || (   ) |
| (____/\| (____/\___) (___|\_)  )  | )   ( || )   ( |
(_______/(_______/\_______/(____/   |/     \||/     \|
                                                      """)

    
    
def get_guess(current_low, current_high):
   return (current_high + current_low)//2
   

def pick_number():
    print (" pick a number  between " + str ( low ) + " and " + str ( high ) + " and I will try and duess it. ")
    ready = input("press enter when you are ready...")
        
def check_guess(guess):
   
    print(" Was " +  str(guess) + " correct? ")
    print()
    print(" type higher if the guess was to low.")
    print()
    print (" type lower if the guess was to high")
    print()
    print("if the guess was right type ok")

    t = input()
    if t == str("higher"):
        return 1
    if t == str("lower"):
        return -1
    if t == str("ok"):
        return 0 


def show_result():
    if t == 0:
        print("yay! you win")
    else:
        print ("you suck!")


def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    result = -1
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess)

        if result == -1:
            # adjust current high
            current_high = guess
        elif result == 1:
            # adjust current low
            current_low = guess

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

