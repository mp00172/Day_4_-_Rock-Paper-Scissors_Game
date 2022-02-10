import random


def winner(p, c):
	if p == c:
		return "It's a draw."
	elif p == "R" and c == "P":
		return "You lose."
	elif p == "R" and c == "S":
		return "You win!"
	elif p == "P" and c == "R":
		return "You win!"
	elif p == "P" and c == "S":
		return "You lose."
	elif p == "S" and c == "R":
		return "You lose."
	elif p == "S" and c == "P":
		return "You win!"


choices = {"R": ["Rock", """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""],
		   "P": ["Paper", """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""],
		   "S": ["Scissors", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""]}

game_is_on = True
player_score = 0
computer_score = 0

while game_is_on:
	player_choice = input("\nWhat's your choice? Type \"R\" for ROCK, \"P\" for PAPER, or \"S\" for SCISSORS: ").upper()
	while player_choice not in choices.keys():
		player_choice = input("Invalid input. Please enter \"R\", \"P\", or \"S\". ").upper()
	computer_choice = random.choice(list(choices.keys()))
	print("\nYou choose {}.".format(choices[player_choice][0]))
	print(choices[player_choice][1])
	print("\nComputer choose {}.".format(choices[computer_choice][0]))
	print(choices[computer_choice][1])

	your_result = winner(player_choice, computer_choice)
	print("\n" + your_result)
	if your_result == "You win!":
		player_score += 1
	elif your_result == "You lose.":
		computer_score += 1
	print("Your score: {}".format(player_score))
	print("Computer score: {}".format(computer_score))

	play_again = input("\nPlay again? \"Y\" or \"N\"? ").upper()
	while play_again not in ["Y", "N"]:
		play_again = input("Invalid input. Please enter \"Y\", or \"N\". ").upper()
	if play_again == "N":
		print("\nGame over. Thank you for playing!")
		game_is_on = False
