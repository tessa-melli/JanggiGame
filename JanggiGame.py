# Author: Tessa Melli
# Date: 3/11/21
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


class Piece:
    """Represents a generic piece"""
    # self._piece_type = 'PIECE'
    # method for get_piece_type
    # self._piece_location = ??
    # method for get_piece_location


class General:
    """Represents the General piece, inherits from the Piece class"""
    # self._piece_type = 'GENERAL'


class Guard:
    """Represents the Guard piece, inherits from the Piece class"""
    # self._piece_type = 'GUARD'


class Horse:
    """Represents the Horse piece, inherits from the Piece class"""
    # self._piece_type = 'HORSE'


class Elephant:
    """Represents the Elephant piece, inherits from the Piece class"""
    # self._piece_type = 'ELEPHANT'


class Chariot:
    """Represents the Chariot piece, inherits from the Piece class"""
    # self._piece_type = 'CHARIOT'


class Cannon:
    """Represents the Cannon piece, inherits from the Piece class"""
    # self._piece_type = 'CANNON'


class Soldier:
    """Represents the Soldier piece, inherits from the Piece class"""
    # self._piece_type = 'Soldier'


class GameBoard:
    """A game board to visualize the current game state"""

    # Contains a depiction of the physical gameboard
    # Also contains the key to translate between the board locations and cartesian coordinates
    # self._letter_to_number = {a:1, b:2, c:3, d:4, e:5, f:6, g:7, h:8, i:9}


class BluePlayer:
    """Represents the Blue player"""


class RedPlayer:
    """Represents the Red player"""


class JanggiGame:
    """"""

    # Initialize data members
    def __init__(self):
        """"""
        self._game_state = 'UNFINISHED'
        self._current_player = 'BLUE'

    # Method called get_game_state that returns 'UNFINISHED', 'RED_WON', or 'BLUE_WON'
    def get_game_state(self):
        """
        Returns the current game state.
        :return: 'UNFINISHED' - if the game is unfinished
                 'RED_WON' if the red player has won
                 'BLUE_WON' if the blue player has won
        """
        return self._game_state

    # Method called is_in_check that takes as a parameter either 'red' or 'blue'
    # and returns True if that player is in check, but returns false otherwise
    def is_in_check(self, player):
        """

        :param player: 'red' or 'blue' for player being assessed for a checkmate
        :return: True - if the player is in check
                 False - if the player is not in check
        """

    # Method called make_move that takes two parameters - strings that
    # represent the square to move from and the square to move to
    def make_move(self, from_location, to_location):
        """

        :param from_location: location to move from
        :param to_location: location to move to
        :return: False - if the move cannot be performed
                 True - if the indicated move is performed
        """

        # Return False:
        #   If the game has already been won
        #   If the square af the from_location does not have a current player's piece
        #   To location has same player's piece
        #   If the indicated move is not legal due to movement rules of piece (valid move method?)
        #   If the indicated move is not legal due to placing the player's general in check (puts in check method?)

        # Otherwise:
        #   Make the indicated move
        #   Remove any captured piece
        #   Assess if the other player's piece is in check by any # of current pieces
        #   Update the game state as necessary (by assessing for checkmate, as necessary)
        #       > See if general can move
        #       > See if another piece can take the offending player's piece(s)
        #       > See if another piece can block the offending player's piece(s)
        #   Update whose turn it is
        #   Return True
