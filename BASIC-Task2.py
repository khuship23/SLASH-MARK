import random
import time
import tkinter as tk
from tkinter import messagebox

number = random.randint(1, 200)

def intro():
    print("May I ask you for your name?")
    name = input() 
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6: 
        enter = entry_guess.get()
        try: 
            guess = int(enter)
            if guess <= 200 and guess >= 1: 
                guessesTaken = guessesTaken + 1 
                if guessesTaken < 6:
                    if guess < number:
                        feedback_label.config(text="The guess is too low")
                    elif guess > number:
                        feedback_label.config(text="The guess is too high")
                    else:
                        messagebox.showinfo("Congratulations!", "You guessed the number!")
                        break
                if guess != number:
                    time.sleep(0.5)
                    feedback_label.config(text="Try Again!")
            else:
                feedback_label.config(text="Please enter a number between 1 and 200")
        except ValueError: 
            feedback_label.config(text="Please enter a valid number.")
            
    if guess != number:
        messagebox.showinfo("Game Over", f"The number I was thinking of was {number}")

def play_again():
    intro()
    pick()
    response = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if response:
        entry_guess.delete(0, tk.END)
        feedback_label.config(text="")
        play_again()
    else:
        root.destroy()

root = tk.Tk()
root.title("Guess the Number")

intro_label = tk.Label(root, text="May I ask you for your name?")
intro_label.pack()

entry_name = tk.Entry(root)
entry_name.pack()

start_button = tk.Button(root, text="Start Game", command=intro)
start_button.pack()

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

submit_button = tk.Button(root, text="Submit Guess", command=pick)
submit_button.pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack()

play_again()

root.mainloop()
