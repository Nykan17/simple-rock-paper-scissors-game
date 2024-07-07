import random

choices = ["rock", "paper", "scissors"]
player = None
computer = random.choice(choices)

player = input("Enter a choice (rock, paper, scissors): ").lower()

print(f"Player: {player}")
print(f"Computer: {computer}")

# Win-loss conditions
if player == computer:
    print("You have been Tied!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You have win!")
else:
    print("You have lose.")