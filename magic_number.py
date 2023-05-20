import os, platform, time

MIN = 1
MAX = 10
REWARD = 10

# PLAYER DATA
CREDITS = 10
PLAYER_NAME = None


def main():
    clear_screen()
    get_player_name()

    intro()

    game_loop()

def intro():
    clear_screen()
    """
    Prints the game title and its rules
    """
    print("-"*50, "MAGIC NUMBER", "-"*50)
    print(f"Wellcome {PLAYER_NAME}!")
    time.sleep(4)

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def game_loop():
    """
    The main game where we ask the player
    """
    clear_screen()
    print(f"I have a number between {MIN} and {MAX}. Can you guess it?")

    magic_number = 5
    max_tries = 3
    print(f"You can try {max_tries} times.")

    player_guess = input("Your guess?")
    while player_guess != str(magic_number):
        clear_screen()
        max_tries -= 1

        if max_tries == 0:
            break

        print(f"Wrong guess. You have {max_tries} tries. Try Again.")
        player_guess = input("Your guess?")
    
    clear_screen()
    
    check_result(magic_number, player_guess)

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def check_result(magic_number, player_guess):
    """
    Check wining conditions
    """
    global CREDITS

    if player_guess == str(magic_number):
        print(f"You wind! {magic_number} was my number :)))")
        CREDITS += REWARD
        print(f"You won {REWARD} credits. Now you have {CREDITS} credits.")
        print("Well done!")
    else:
        print(f"My number was {magic_number}.")
        CREDITS -= REWARD
        print(f"You lost {REWARD} credits. You have {CREDITS} left.")
    
    restart_game()

def restart_game():
    """
    Ask player if he/she wants to continue the game.
    """
    if CREDITS < 0:
        exit_game()
    else:
        player_response = input("Do you want to try again? (y/n)").lower()
        if player_response == "y":
            game_loop()
        else:
            exit_game()
        

def exit_game():
    """
    Exit game
    """
    print("Maybe next time :)")
    exit()


main()