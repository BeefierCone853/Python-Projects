import os

end_game = False
number_of_turns = 0
number = 0
player_character = 'X'
winning_combinations = {1: [1, 5, 9],
                        2: [26, 30, 34],
                        3: [51, 55, 59],
                        4: [1, 26, 51],
                        5: [5, 30, 55],
                        6: [9, 34, 39],
                        7: [1, 30, 59],
                        8: [9, 30, 51]}

# Marked board to represent places on the board with numbers (reference for players)
marked_board = " 1 | 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 \n"

# The actual board on which Xs and Os are placed (whitespace is replaced with 'X' or 'O')
game_board = "   |   |   \n------------\n   |   |   \n------------\n   |   |   "


# Check if game is over after every turn
def game_over(board):
    x_positions = []
    o_positions = []
    end_of_game = False

    index_positions = []
    position_number = 0
    for char_ in board:
        if char_ == 'O':
            o_positions.append(position_number)

        if char_ == 'X':
            x_positions.append(position_number)
        position_number += 1

    x_positions.sort()
    o_positions.sort()

    for list_ in winning_combinations.values():
        end_of_game = all(i in x_positions for i in list_)
        if end_of_game:
            print(50 * '\n')
            print("\nPlayer 'X' has won. Congratulations!")
            print(board)
            break

        end_of_game = all(i in o_positions for i in list_)
        if end_of_game:
            print(50 * '\n')
            print("\nPlayer 'O' has won. Congratulations!")
            print(board)
            break

    return end_of_game


print("Welcome to the Tic Tac Toe game.")
print("This is the design of the board: ")
print(marked_board)

ready_to_play = input("Each number represents a place on the board.\n"
                      "To place 'X' or 'O', type the number of the corresponding place on the board.\n"
                      "Type 'Ready' when you want to start playing.\n").lower()

while end_game is False:
    if ready_to_play == 'ready':
        correct_number = False

        print(50 * '\n')
        print(f"{marked_board}\n")

        if number_of_turns % 2 == 0:
            player_character = 'X'
            print(f"Player {player_character}'s turn: ")
        else:
            player_character = 'O'
            print(f"Player {player_character}'s turn: ")

        print(game_board)

        while correct_number is False:
            number = input()
            position_of_number = (marked_board.find(number))

            # Check if the correct place on the board was entered (1-9)
            if position_of_number == -1:
                print("Incorrect character, please refer to the board with numbers for each place.")

            else:
                number_of_chars = 0
                for char in game_board:

                    # Check if an 'X' or 'O' is already placed on the entered position
                    if number_of_chars == position_of_number:
                        if char != ' ':
                            print("An 'X' or 'O' is already placed on that position.\n"
                                  "Please choose an empty position: ")
                        else:
                            correct_number = True
                        break
                    number_of_chars += 1

                # If both of the previous checks were passed, replace the whitespace on the game board
                # with the player character ('X' or 'O')
                if correct_number:
                    game_board = game_board[:position_of_number] + player_character + \
                                 game_board[position_of_number + 1:]
                    number_of_turns += 1

                # Check if game is over
                end_game = game_over(game_board)
                if number_of_turns == 8:
                    print(50 * '\n')
                    print("It's a draw!")
                    print(game_board)
                    end_game = True

    else:
        ready_to_play = input("Incorrect input. Type 'Ready' when you want to start playing.\n")
