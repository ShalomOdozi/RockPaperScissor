from random import randint



def play_game():
    option = ["Rock", "Paper", "Scissors"]
    computer = option[randint(0, 2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "wraps", player)
            else:
                print("You win")
        elif player == "Paper":
            if computer == "Scissor":
                print("You lose", computer, "cut", player)
            else:
                print("You win")

        elif player == "Scissor":
            if computer == "Rock":
                print("You lose", computer, "crushes", player)
            else:
                print("You win")
        else:
            print("That's not valid, check again")