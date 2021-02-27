# Author: Tessa Melli
# Date:
# Description:

# Write a class named JanggiGame for playing an abstract board came called Janggi

# DO NOT NEED TO IMPLEMENT
#   perpetual check
#   position repetition
#   draw
#   miscellaneous rules

# DO NEED:
#   checkmate
#   piece-specific rules
#       generals aren't allowed to leave the palaces
#       horses and elephants can be blocked
#           * blocking occurs if a piece is in any part of the move by either opponents or own piece
#       cannons cannot capture other cannons
#   cannot make a move that puts or leaves their general in check


class JanggiGame:
    """"""

    # Initialize data members
    def __init__(self):
        """"""

    # Method called get_game_state that returns 'UNFINISHED', 'RED_WON', or 'BLUE_WON'
    def get_game_state(self):
        """"""

    # Method called is_in_check that takes as a parameter either 'red' or 'blue'
    # and returns True if that player is in check, but returns false otherwise
    def is_in_check(self, player):
        """"""

    # Method called make_move that takes two parameters - strings that
    # represent the square to move from and the square to move to
    def make_move(self, from_square, to_square):
        """"""

        # Return False:
        #   If the square being moved from does not contain a piece belonging to the player whose turn it is
        #   If the indicated move is not legal
        #   If the game has already been won

        # Otherwise:
        #   Make the indicated move
        #   Remove any captured piece
        #   Update the game state is necessary
        #   Update whose turn it is
        #   Return True