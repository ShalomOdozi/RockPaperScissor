from rps import play_game

play_again = True
play_game()

while play_again:
    print("Do you want to play again? Y for yes and N for no")
    choice = input().lower()

    if choice == "y":
        play_game()

    elif choice == "n":
        play_again = False

