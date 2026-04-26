# main.py

from game import play_game

while True:
    print("\n====== DICE ROLL GAME MENU ======")
    print("1. Play Game")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        play_game()

    elif choice == 2:
        print("Thank you for playing!")
        break

    else:
        print("Invalid Choice. Please try again.")