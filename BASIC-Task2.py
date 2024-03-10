import random
import time

def greeting():
    print("Hey there! What's your name?")
    name = input("Enter your name: ")
    print(f"Hello {name}! Let's play a fun game. I've selected a number between 1 and 200.")
    time.sleep(0.5)
    print("Try to guess it!")

def select_number():
    number = random.randint(1, 200)
    attempts = 0
    while attempts < 6:
        time.sleep(0.25)
        user_input = input("Your guess: ")
        try:
            guess = int(user_input)
            if 1 <= guess <= 200:
                attempts += 1
                if attempts < 6:
                    if guess < number:
                        print("Too low! Try again.")
                    elif guess > number:
                        print("Too high! Try again.")
                    else:
                        print("Congratulations! You've guessed it right!")
                        return True
                else:
                    print("Out of attempts! The number was:", number)
                    return False
            else:
                print("Your guess is out of range. Please choose a number between 1 and 200.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Out of attempts! The number was:", number)
    return False

def play_game():
    play = "yes"
    while play.lower() in {"yes", "y"}:
        greeting()
        if not select_number():
            break
        print("Want to play again? (yes/no)")
        play = input().lower()

if __name__ == "__main__":
    play_game()
