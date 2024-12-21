import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x200")

        self.player_score = 0
        self.computer_score = 0

        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Player").grid(row=0, column=0)
        tk.Label(self.root, text="Computer").grid(row=0, column=2)
        tk.Label(self.root, textvariable=self.player_choice).grid(row=1, column=0)
        tk.Label(self.root, textvariable=self.computer_choice).grid(row=1, column=2)

        tk.Label(self.root, text="Player Score:").grid(row=2, column=0)
        tk.Label(self.root, textvariable=str(self.player_score)).grid(row=2, column=1)
        tk.Label(self.root, text="Computer Score:").grid(row=2, column=2)
        tk.Label(self.root, textvariable=str(self.computer_score)).grid(row=2, column=3)

        tk.Label(self.root, textvariable=self.result).grid(row=3, column=1)

        tk.Button(self.root, text="Rock", command=lambda: self.play("rock")).grid(row=4, column=0)
        tk.Button(self.root, text="Paper", command=lambda: self.play("paper")).grid(row=4, column=1)
        tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors")).grid(row=4, column=2)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        self.player_choice.set(player_choice)
        self.computer_choice.set(computer_choice)

        if player_choice == computer_choice:
            self.result.set("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_score += 1
            self.result.set("You win!")
        else:
            self.computer_score += 1
            self.result.set("Computer wins!")

        self.update_scores()

    def update_scores(self):
        self.root.children['!label'].config(text=f"Player Score: {self.player_score}")
        self.root.children['!label2'].config(text=f"Computer Score: {self.computer_score}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.root.mainloop()