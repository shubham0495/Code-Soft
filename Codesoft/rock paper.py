import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        # Create buttons for user choices
        self.button_rock = tk.Button(self.root, text="Rock", command=lambda: self.play('rock'))
        self.button_rock.pack(pady=10)
        
        self.button_paper = tk.Button(self.root, text="Paper", command=lambda: self.play('paper'))
        self.button_paper.pack(pady=10)
        
        self.button_scissors = tk.Button(self.root, text="Scissors", command=lambda: self.play('scissors'))
        self.button_scissors.pack(pady=10)
        
        # Create labels for displaying scores
        self.label_user_score = tk.Label(self.root, text=f"Your Score: {self.user_score}")
        self.label_user_score.pack(pady=5)
        
        self.label_computer_score = tk.Label(self.root, text=f"Computer Score: {self.computer_score}")
        self.label_computer_score.pack(pady=5)
        
    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        # Determine the result
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update scores based on result
        if result == 'win':
            self.user_score += 1
            message = f"You chose {user_choice}. Computer chose {computer_choice}.\nYou win!"
        elif result == 'lose':
            self.computer_score += 1
            message = f"You chose {user_choice}. Computer chose {computer_choice}.\nYou lose!"
        else:
            message = f"You chose {user_choice}. Computer chose {computer_choice}.\nIt's a tie!"
        
        # Update score labels
        self.label_user_score.config(text=f"Your Score: {self.user_score}")
        self.label_computer_score.config(text=f"Computer Score: {self.computer_score}")
        
        # Show result in a messagebox
        messagebox.showinfo("Result", message)
        
        # Ask if user wants to play again
        if messagebox.askyesno("Play Again", "Do you want to play another round?"):
            return
        else:
            self.root.quit()
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'win'
        else:
            return 'lose'

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
