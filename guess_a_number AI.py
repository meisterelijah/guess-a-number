import random
import math



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
    print(" what is your name? ")
    guest_name = input()
    return guest_name
    
  
def show_credits():
    print(""" This game was created by.......
_______  _       __________________ _______          
(  ____ \( \      \__   __/\__    _/(  ___  )|\     /|
| (    \/| (         ) (      )  (  | (   ) || )   ( |
| (__    | |         | |      |  |  | (___) || (___) |
|  __)   | |         | |      |  |  |  ___  ||  ___  |
| (      | |         | |      |  |  | (   ) || (   ) |
| (____/\| (____/\___) (___|\_)  )  | )   ( || )   ( |
(_______/(_______/\_______/(____/   |/     \||/     \|
                                                      """)

    
def get_tries(current_low, current_high):
    tries = math.ceil(math.log(((int(current_high) - int(current_low))-1),2))
    return tries 
                      
def get_guess(current_low, current_high):
   return (int(current_low) + int(current_high))//2
   
def pick_low():
    print (" what would you like to be the low?")
    low = input()
    return low

def pick_high():
    print("What would you like the high to be?")
    high = input()
    return high

    
    
def pick_number(current_low, current_high):
    print (" pick a number  between " + str ( current_low ) + " and  " +  str ( current_high )  + " " + ( guest_name )  +  "  and I will try and duess it. ")
    ready = input("press enter when you are ready " + ( guest_name ) + "...")
        
def check_guess(guess, guest_name):
   
    print(" Was " +  str(guess) + " correct" + (guest_name) + " ? " )
    print()
    print(" type higher if the guess was to low.")
    print()
    print (" type lower if the guess was to high")
    print()
    print("if the guess was right type ok")

    d = input()
    d = d.lower()
    if d == str("higher"):
        return 1
    if d == str("lower"):
        return -1
    if d == str("ok"):
        return 0


def show_result():
    pass


def play_again():
    print( " I won!YAY!!")
    
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
      
            
def state_tries(tries):
    print(" I guess the number in" + str(tries) +" tries.")
  
def play():
    current_low = pick_low()
    current_high = pick_high()
    result = -1
    
    pick_number(current_low, current_high)
    tries = get_tries(current_low, current_high)
    state_tries(tries)
    
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess, guest_name)

        if result == -1:
            # adjust current high
            current_high = guess
        elif result == 1:
            # adjust current low
            current_low = guess

    show_result()

# Game starts running here
guest_name = show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

