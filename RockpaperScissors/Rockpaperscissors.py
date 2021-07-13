
import random

# list of choice

choice = ["rock", 'paper', "scissor"]

computer = random.choice(choice)
user = False


def rps_input():
    user = input("Enter r | p | s")
    if user == computer:
        return "Tie"


def rps(player1, player2):
    rps_input()
    if (player1 == 'r' and player2 == 's'):
        return 'Rock crushes scissor!'
    elif player1 == 's' and player2 == 'p':
        return 'Scissor cut paper!'
    elif player1 == 'p' and player2 == 'r':
        return "Paper covers rock"
    else:
        return 'You fail'


print(rps(user, computer))
print(computer)
