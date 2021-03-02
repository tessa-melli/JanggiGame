# Author: Tessa Melli
# Date: 3/11/21
# Description:

# Write a class named JanggiGame for playing an abstract board came called Janggi


class Piece:
    """Represents a generic piece"""
    # self._piece_type = 'PIECE'
    # method for get_piece_type
    # self._piece_location = ??
    # method for get_piece_location
    # method for set_piece_location

    def __init__(self, piece_type, location, cartesian, color):
        self._piece_info = {'type': piece_type,
                            'color': color,
                            'location': location,
                            'cartesian': cartesian,
                            'checking': False}

        self._letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

    def get_type(self):
        return self._piece_info['type']

    def get_color(self):
        return self._piece_info['color']

    def get_location(self):
        return self._piece_info['location']

    def set_location(self, new_location):
        self._piece_info['location'] = new_location

    def get_cartesian(self):
        return self._piece_info['cartesian']

    def set_cartesian(self, new_location):
        self._piece_info['cartesian'] = new_location

    def get_is_checking(self):
        return self._piece_info['checking']

    def set_is_checking(self, checking):
        self._piece_info['checking'] = checking


class General:
    """Represents the General piece, inherits from the Piece class"""
    # self._piece_type = 'GENERAL'
    # May move one step per turn along marked board lines to any of the nine points within the palace
    # General cannot leave the palace
    # Can choose to make no move


class Guard:
    """Represents the Guard piece, inherits from the Piece class"""
    # self._piece_type = 'GUARD'
    # Move the same as the general
    # Cannot leave the palace


class Horse:
    """Represents the Horse piece, inherits from the Piece class"""
    # self._piece_type = 'HORSE'
    # moves one step orthogonally, then one step diagonally outward
    # no jumping (can be blocked - up to 2 spots)


class Elephant:
    """Represents the Elephant piece, inherits from the Piece class"""
    # self._piece_type = 'ELEPHANT'
    # move one point orthogonally followed by two points diagonally
    # blocked by any intervening pieces (up to 3 spots)


class Chariot:
    """Represents the Chariot piece, inherits from the Piece class"""
    # self._piece_type = 'CHARIOT'
    # moves and captures in a straight line (horizontally or vertically)
    # May move along diagonal lines inside either palace


class Cannon:
    """Represents the Cannon piece, inherits from the Piece class"""
    # self._piece_type = 'CANNON'
    # moves by jumping another piece horizontally or vertically
    # must be exactly one piece (friendly or otherwise) between from & to position
    # cannot jump over or capture another cannon
    # can jump diagonally w/in the palace


class Soldier:
    """Represents the Soldier piece, inherits from the Piece class"""
    # self._piece_type = 'Soldier'
    # move one point forward or sideways
    # can move diagonally forward w/in enemy palace


class GameBoard:
    """A game board to visualize the current game state"""

    # Contains a depiction of the physical game board
    # Also contains the key to translate between the board locations and cartesian coordinates
    #

    def __init__(self):
        self._game_board = [
            ['0 ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['2 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['6 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['8 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['9 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['10', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]


class BluePlayer:
    """Represents the Blue player"""
    # has a list(?) containing all of the blue Pieces
    def __init__(self):
        self._blue_pieces = {'blue_general': General(),
                             'blue_guard_1': Guard(), 'blue_guard_2': Guard(),
                             'blue_horse_1': Horse(), 'blue_horse_2': Horse(),
                             'blue_elephant_1': Elephant(), 'blue_elephant_2': Elephant(),
                             'blue_chariot_1': Chariot(), 'blue_chariot_2': Chariot(),
                             'blue_cannon_1': Cannon(), 'blue_cannon_2': Cannon(),
                             'blue_soldier_1': Soldier(), 'blue_soldier_2': Soldier(),
                             'blue_soldier_3': Soldier(), 'blue_soldier_4': Soldier(),
                             'blue_soldier_5': Soldier()}


class RedPlayer:
    """Represents the Red player"""

    def __init__(self):
        self._red_pieces = {'red_general': General(),
                            'red_guard_1': Guard(), 'red_guard_2': Guard(),
                            'red_horse_1': Horse(), 'red_horse_2': Horse(),
                            'red_elephant_1': Elephant(), 'red_elephant_2': Elephant(),
                            'red_chariot_1': Chariot(), 'red_chariot_2': Chariot(),
                            'red_cannon_1': Cannon(), 'red_cannon_2': Cannon(),
                            'red_soldier_1': Soldier(), 'red_soldier_2': Soldier(),
                            'red_soldier_3': Soldier(), 'red_soldier_4': Soldier(),
                            'red_soldier_5': Soldier()
                            }


class JanggiGame:
    """"""

    # Initialize data members
    def __init__(self):
        """"""
        self._game_state = 'UNFINISHED'
        self._current_player = 'BLUE'
        self._game_board = GameBoard()
        self._blue_player = BluePlayer()
        self._red_player = RedPlayer()

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
