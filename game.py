# import random is needed for the computer to choose its answer from
import random

print("Rock-Paper-Scissors Game")

# declares the score variables of the player and the computer
player_score = 0
computer_score = 0

# computer chooses from the list for answers using the random function
options = ["ROCK", "PAPER", "SCISSORS"]

rounds = int(input("How many rounds would you like to play? "))

# FUNCTION OF THE GAME, rounds inputted decide how many rounds there will be
for i in range(rounds):
    
    # every instance of the for loop, the round asks the player for new input and the opponent variable changes value
    player = str(input("Enter your choice: ")).upper()
    opponent = random.choice(options)

    if (player == "ROCK"):
        if (opponent == "ROCK"):
            print("Opponent chose rock")
            print("Tie")
        elif (opponent == "SCISSORS"):
            print("Opponent chose scissors")
            print("Player wins.")
            player_score = player_score + 1
        elif (opponent == "PAPER"):
            print("Opponent chose paper")
            print("Opponent wins.")
            computer_score = computer_score + 1
        else:
            print("Invalid input. Will not be counted")
    elif (player == "SCISSORS"):
        if (opponent == "ROCK"):
            print("Opponent chose rock")
            print("Opponent wins.")
            computer_score = computer_score + 1
        elif (opponent == "SCISSORS"):
            print("Opponent chose scissors")
            print("Tie.")
        elif (opponent == "PAPER"):
            print("Opponent chose paper")
            print("Player wins.")
            player_score = player_score + 1
        else:
            print("Invalid input. Will not be counted")
    elif (player == "PAPER"):
        if (opponent == "ROCK"):
            print("Opponent chose rock")
            print("Player wins.")
            player_score = player_score + 1
        elif (opponent == "SCISSORS"):
            print("Opponent chose scissors")
            print("Opponent wins.")
            computer_score = computer_score + 1
        elif (opponent == "PAPER"):
            print("Opponent chose paper")
            print("Tie.")
        else:
            print("Invalid input. Will not be counted")
    else:
        print("Invalid input. Try again.")

# CHECKS WHO WON THE GAME
if (player_score > computer_score):
    print("Player wins the game.")
elif(player_score < computer_score):
    print("Computer wins the game.")
else:
    print("The game ends in a tie.")

# PRINTS THE SCORES
print("SCORES:")
print("Player got a score of", player_score)
print("Computer got a score of", computer_score)