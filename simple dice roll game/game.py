# game.py

from dice import roll_dice

def play_game():
    print("\n----- DICE ROLL GAME -----")
    
    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")

    print("\nRolling dice for", player1, "...")
    p1 = roll_dice()
    print(player1, "got:", p1)

    print("\nRolling dice for", player2, "...")
    p2 = roll_dice()
    print(player2, "got:", p2)

    if p1 > p2:
        print("\nWinner is:", player1)

    elif p2 > p1:
        print("\nWinner is:", player2)

    else:
        print("\nMatch Draw!")