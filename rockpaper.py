import tkinter as tk
from tkinter import messagebox
import random

def winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Paper") or \
         (player == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "You Lose!"

def play_game(player):
    global rounds_played, user_score, computer_score
    
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    result = winner(player, computer)
    
    result_label.config(text=f"Computer chose: {computer}\n{result}")

    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")
    
    rounds_played += 1
    rounds_label.config(text=f"Round: {rounds_played}/5")
    
    if rounds_played >= 5:
        if user_score > computer_score:
            final_result = "You are the overall winner!"
        elif user_score < computer_score:
            final_result = "Computer is the overall winner!"
        else:
            final_result = "It's an overall tie!"
        
        messagebox.showinfo("Game Over", final_result)
        continue_game()

def continue_game():
    global rounds_played, user_score, computer_score
    
    response = messagebox.askyesnocancel("Game Over", "Do you want to continue playing?\nClick 'Yes' to continue, 'No' to start a new game, or 'Cancel' to exit.")
    
    if response is None:
        root.destroy()
    elif response:
        rounds_played = 0
        rounds_label.config(text=f"Round: {rounds_played}/5")
    else:
        rounds_played = 0
        user_score = 0
        computer_score = 0
        score_label.config(text="User: 0  Computer: 0")
        rounds_label.config(text=f"Round: {rounds_played}/5")

user_score = 0
computer_score = 0
rounds_played = 0

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")
root.configure(bg="dark slate gray")

instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16, "bold"), fg="turquoise", bg="dark slate gray")
instructions.pack(pady=10)

button_frame = tk.Frame(root, bg="dark slate gray")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14, "bold"), fg="black", bg="red", width=10, command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14, "bold"), fg="black", bg="sky blue", width=10, command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14, "bold"), fg="black", bg="yellow", width=10, command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="turquoise", bg="dark slate gray")
result_label.pack(pady=20)

score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Helvetica", 14, "bold"), fg="light sky blue", bg="dark slate gray")
score_label.pack(pady=10)

rounds_label = tk.Label(root, text="Round: 0/5", font=("Helvetica", 14, "bold"), fg="light sky blue", bg="dark slate gray")
rounds_label.pack(pady=10)

root.mainloop()
