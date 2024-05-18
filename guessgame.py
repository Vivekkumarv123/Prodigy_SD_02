import tkinter as tk
from tkinter import messagebox
import random

# Generate the random number
random_number = random.randint(1, 100)
attempts = 0

# Define the guess function
def guess_number():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < random_number:
            result_label.config(text="Too low! Try again.", fg='#ff6f61')
        elif guess > random_number:
            result_label.config(text="Too high! Try again.", fg='#ff6f61')
        else:
            result_label.config(text=f"Congratulations! You guessed the number {random_number} in {attempts} attempts.", fg='#3cb371')
            messagebox.showinfo("Game Over", f"You guessed the number in {attempts} attempts!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

# Set up the main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("600x500")
root.configure(bg='#f0f8ff')

# Set up the font
font_large = ("Comic Sans MS", 24, "bold")
font_medium = ("Comic Sans MS", 16)
font_small = ("Comic Sans MS", 14)

# Create and place the widgets
title_label = tk.Label(root, text="🎉 Guess the Number Game 🎉", font=font_large, bg='#f0f8ff', fg='#ff4500')
title_label.pack(pady=20)

instructions_label = tk.Label(root, text="I have selected a number between 1 and 100. Can you guess it?", font=font_medium, bg='#f0f8ff', fg='#4682b4')
instructions_label.pack(pady=10)

entry = tk.Entry(root, font=font_medium, width=10, justify='center', bd=3)
entry.pack(pady=20)

guess_button = tk.Button(root, text="Guess", font=font_medium, command=guess_number, bg='#ffa07a', fg='white', bd=0, relief='solid')
guess_button.pack(pady=10)

result_label = tk.Label(root, text="", font=font_small, bg='#f0f8ff')
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
