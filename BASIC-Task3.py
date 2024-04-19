import random
import tkinter as tk
from tkinter import messagebox

def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 
    for length in pwlength:
        password = "" 
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password) 
    return passwords

def replaceWithNumber(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword

def replaceWithUppercaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword

def generate_passwords():
    try:
        numPasswords = int(entry_num_passwords.get())
        passwordLengths = [int(length) if int(length) >= 3 else 3 for length in entry_password_lengths.get().split(",")]

        passwords = generatePassword(passwordLengths)

        result_text.delete(1.0, tk.END)
        for i, password in enumerate(passwords):
            result_text.insert(tk.END, f"Password #{i+1}: {password}\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input")

root = tk.Tk()
root.title("Password Generator")

label_num_passwords = tk.Label(root, text="How many passwords do you want to generate?")
label_num_passwords.pack()

entry_num_passwords = tk.Entry(root)
entry_num_passwords.pack()

label_password_lengths = tk.Label(root, text="Enter the length(s) of password(s) separated by comma (,)")
label_password_lengths.pack()

entry_password_lengths = tk.Entry(root)
entry_password_lengths.pack()

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()
