# Author: Tessa Melli
# Date: 3/11/21
# Description:


class Piece:
    """
    Represents a generic piece with methods associated with all pieces regardless of type
    Each piece type class inherits from this Piece class
    """

    def __init__(self, location, color, nickname):
        """
        Initializes the generic piece object
        :param location: piece's location on the board
        :param color: color of the piece
        :param nickname: nickname of the piece for the game board representation
        """
        self._piece_color = color
        self._piece_location = location
        self._piece_nickname = nickname
        self._checking = False  # stores status of piece checking opponent's general
        self._blue_palace = [[8, 4], [10, 4], [9, 5], [8, 6], [10, 6], [9, 4], [8, 5], [10, 5], [9, 6]]
        self._red_palace = [[1, 4], [3, 4], [2, 5], [1, 6], [3, 6], [2, 4], [1, 5], [3, 5], [2, 6]]

    def get_color(self):
        """
        Getter method for piece color
        :return: color of the piece
        """
        return self._piece_color

    def get_location(self):
        """
        Getter method for the piece location
        :return: piece location in algebraic notation
        """
        return self._piece_location

    def set_location(self, new_location):
        """
        Setter method for the piece location
        :param new_location: new piece location in algebraic notation
        """
        self._piece_location = new_location

    def get_nickname(self):
        """
        Getter method for piece nickname
        :return: nickname for piece to use for the game board representation
        """
        return self._piece_nickname

    def get_is_checking(self):
        """
        Getter method for the checking status of the piece
        :return: True - if the piece is currently checking the opponent's general
                 False - if the piece is not currently checking the opponent's general
        """
        return self._checking

    def set_is_checking(self, checking_status):
        """
        Setter method for the checking status of the piece
        :param checking_status: True/False depending on if the piece is checking the opponent's general
        """
        self._checking = checking_status

    def get_palace(self, directionality):
        """

        :param directionality:
        :return:
        """

        if directionality == 1:
            return self._red_palace
        elif directionality == -1:
            return self._blue_palace
        else:
            return None


class General(Piece):
    """
    Represents the General piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname, directionality):
        """
        Initializes the General object
        :param location: location of the General piece
        :param color: color of the General piece
        :param directionality: directionality of the General piece (determines which palace it belongs to)
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'GENERAL'
        self._directionality = directionality



    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'GENERAL'
        """
        return self._piece_type

    def get_directionality(self):
        """
        Getter method for the General directionality
        :return: directionality for the General piece
        """
        return self._directionality

    def valid_move(self, from_cartesian, to_cartesian, directionality):
        """

        :param from_cartesian:
        :param to_cartesian:
        :param directionality:
        :return:
        """

        # Trying to move guard out of the palace
        if to_cartesian not in self.get_palace(directionality):
            return False

        # if in one of the corners or in the center position:
        if from_cartesian in self.get_palace(directionality)[0:4]:
            if not (abs(from_cartesian[0] - to_cartesian[0]) <= 1 and abs(from_cartesian[1] - to_cartesian[1]) <= 1):
                return False
        # if currently on one of the 4 side positions
        else:
            if not abs(from_cartesian[0] - to_cartesian[0]) + abs(from_cartesian[1] - to_cartesian[1]) == 1:
                return False

        return True

class Guard(Piece):
    """
    Represents the Guard piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname, directionality):
        """
        Initializes the Guard object
        :param location: location of the Guard piece
        :param color: color of the Guard piece
        :param directionality: directionality of the Guard piece (determines which palace it belongs to)
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'GUARD'
        self._directionality = directionality

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'GUARD'
        """
        return self._piece_type

    def get_directionality(self):
        """
        Getter method for the Guard directionality
        :return: directionality for the Guard piece
        """
        return self._directionality

    def valid_move(self, from_cartesian, to_cartesian, directionality):
        """

        :param from_cartesian:
        :param to_cartesian:
        :param directionality:
        :return:
        """

        # Trying to move guard out of the palace
        if to_cartesian not in self.get_palace(directionality):
            return False

        # if in one of the corners or in the center position:
        if from_cartesian in self.get_palace(directionality)[0:4]:
            if not (abs(from_cartesian[0] - to_cartesian[0]) <= 1 and abs(from_cartesian[1] - to_cartesian[1]) <= 1):
                return False
        # if currently on one of the 4 side positions
        else:
            if not abs(from_cartesian[0] - to_cartesian[0]) + abs(from_cartesian[1] - to_cartesian[1]) == 1:
                return False

        return True


class Horse(Piece):
    """
    Represents the Horse piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname):
        """
        Initializes the Horse object
        :param location: location of the Horse piece
        :param color: color of the Horse piece
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'HORSE'

        self._move_conditions = []
        # TBD data structure that will hold move conditions for the horse piece
        #   moves one step orthogonally, then one step diagonally outward
        #   no jumping (can be blocked - up to 2 spots)

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'HORSE'
        """
        return self._piece_type

    def get_move_conditions(self):
        """
        Getter method for the Horse move conditions
        :return: move conditions for the Horse
        """
        return self._move_conditions


class Elephant(Piece):
    """
    Represents the Elephant piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname):
        """
        Initializes the Elephant object
        :param location: location of the Elephant piece
        :param color: color of the Elephant piece
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'ELEPHANT'

        self._move_conditions = []
        # TBD data structure that will hold move conditions for the Elephant piece
        #   move one point orthogonally followed by two points diagonally
        #   blocked by any intervening pieces (up to 3 spots)
        #   can choose to skip turn (as long as General is not already in check)

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'ELEPHANT'
        """
        return self._piece_type

    def get_move_conditions(self):
        """
        Getter method for the Elephant move conditions
        :return: move conditions for the Elephant
        """
        return self._move_conditions


class Chariot(Piece):
    """
    Represents the Chariot piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname):
        """
        Initializes the Chariot object
        :param location: location of the Chariot piece
        :param color: color of the Chariot piece
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'CHARIOT'

        self._move_conditions = []
        # TBD data structure that will hold move conditions for the Chariot piece
        #   moves and captures in a straight line (horizontally or vertically)
        #   may move along diagonal lines inside either palace
        #   can choose to skip turn (as long as General is not already in check)

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'CHARIOT'
        """
        return self._piece_type

    def get_move_conditions(self):
        """
        Getter method for the Chariot move conditions
        :return: move conditions for the Chariot
        """
        return self._move_conditions


class Cannon(Piece):
    """
    Represents the Cannon piece
    Inherits from the Piece class
    """

    def __init__(self, location, color, nickname):
        """
        Initializes the Cannon object
        :param location: location of the Cannon piece
        :param color: color of the Cannon piece
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'CANNON'

        self._move_conditions = []
        # TBD data structure that will hold move conditions for the Cannon piece
        #   moves by jumping another piece horizontally or vertically
        #   must be exactly one piece (friendly or otherwise) between from & to position
        #   cannot jump over or capture another cannon
        #   can jump diagonally w/in the palace
        #   can choose to skip turn (as long as General is not already in check)

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'CANNON'
        """
        return self._piece_type

    def get_move_conditions(self):
        """
        Getter method for the Cannon move conditions
        :return: move conditions for the Cannon
        """
        return self._move_conditions


class Soldier(Piece):
    """
    Represents the Soldier piece
        > Inherits from the Piece class
        > Each player class will store five of these piece objects
        > JanggiGame class will use the get_piece_type, get_move_conditions, and get_directionality methods
    """

    def __init__(self, location, color, nickname, directionality):
        """
        Initializes the Soldier object
        :param location: location of the Soldier piece
        :param color: color of the Soldier piece
        :param directionality: directionality of the Soldier piece (determines which direction it can move)
        """
        super().__init__(location, color, nickname)
        self._piece_type = 'SOLDIER'
        self._directionality = directionality

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'SOLDIER'
        """
        return self._piece_type

    def get_directionality(self):
        """
        Getter method for the Soldier directionality
        :return: directionality for the Soldier piece
        """
        return self._directionality

    def valid_move(self, from_cartesian, to_cartesian, directionality):
        """

        :param from_cartesian:
        :param to_cartesian:
        :param directionality:
        :return:
        """

        if abs(from_cartesian[1] - to_cartesian[1]) > 1:
            return False

        if not (to_cartesian[0] - from_cartesian[0] == 0 or
                directionality * (to_cartesian[0] - from_cartesian[0]) == 1):
            return False

        # if in diagonals or center of palace:
        if from_cartesian in self.get_palace(1)[0:4] or from_cartesian in self.get_palace(-1)[0:4]:
            # add ability to go diagonally
            if abs(to_cartesian[0] - from_cartesian[0]) + abs(to_cartesian[1] - from_cartesian[1]) > 2:
                return False

        # if not:
        else:
            if abs(to_cartesian[0] - from_cartesian[0]) + abs(to_cartesian[1] - from_cartesian[1]) > 1:
                return False


class GameBoard:
    """
    Represents a game board to visualize the current game state
    """

    def __init__(self):
        """
        Initializes the visual representation of the game board with pieces at their starting locations
        """
        self._game_board = [
            [' 0  ', '  a   ', '  b   ', '  c   ', '  d   ', '  e   ', '  f   ', '  g   ', '  h   ', '  i   '],
            [' 1  ', ' RCh1 ', ' REl1 ', ' RHs1 ', ' RGd1 ', '      ', ' RGd2 ', ' REl2 ', ' RHs2 ', ' RCh2 '],
            [' 2  ', '      ', '      ', '      ', '      ', ' RGen ', '      ', '      ', '      ', '      '],
            [' 3  ', '      ', ' RCn1 ', '      ', '      ', '      ', '      ', '      ', ' RCn2 ', '      '],
            [' 4  ', ' RSr1 ', '      ', ' RSr2 ', '      ', ' RSr3 ', '      ', ' RSr4 ', '      ', ' RSr5 '],
            [' 5  ', '      ', '      ', '      ', '      ', '      ', '      ', '      ', '      ', '      '],
            [' 6  ', '      ', '      ', '      ', '      ', '      ', '      ', '      ', '      ', '      '],
            [' 7  ', ' BSr1 ', '      ', ' BSr2 ', '      ', ' BSr3 ', '      ', ' BSr4 ', '      ', ' BSr5 '],
            [' 8  ', '      ', ' BCn1 ', '      ', '      ', '      ', '      ', '      ', ' BCn2 ', '      '],
            [' 9  ', '      ', '      ', '      ', '      ', ' BGen ', '      ', '      ', '      ', '      '],
            [' 10 ', ' BCh1 ', ' BEl1 ', ' BHs1 ', ' BGd1 ', '      ', ' BGd2 ', ' BEl2 ', ' BHs2 ', ' BCh2 ']
        ]

    def modify_game_board(self, row_index, column_index, new_value):
        """
        Method used to modify the board after each player's turn
        :param row_index: row index of location to modify
        :param column_index: column index of location to modify
        :param new_value: new value for the specified board location
        """
        pass

        self._game_board[row_index][column_index] = new_value

    def print_game_board(self):
        """
        Method that prints each row of the game board on a separate line.
        Used for visualization/troubleshooting purposes only.
        """
        for board_row in self._game_board:
            print(board_row)
        print('')


class BluePlayer:
    """
    Represents the Blue player
    """

    def __init__(self):
        """Initializes the blue player's pieces"""
        self._blue_pieces = {'BlueGeneral': General('e9', 'BLUE', ' BGen ', -1),
                             'BlueGuard1': Guard('d10', 'BLUE', ' BGd1 ', -1),
                             'BlueGuard2': Guard('f10', 'BLUE', ' BGd2 ', -1),
                             'BlueHorse1': Horse('c10', 'BLUE', ' BHs1 '),
                             'BlueHorse2': Horse('h10', 'BLUE', ' BHs2 '),
                             'BlueElephant1': Elephant('b10', 'BLUE', ' BEl1 '),
                             'BlueElephant2': Elephant('g10', 'BLUE', ' BEl2 '),
                             'BlueChariot1': Chariot('a10', 'BLUE', ' BCh1 '),
                             'BlueChariot2': Chariot('i10', 'BLUE', ' BCh2 '),
                             'BlueCannon1': Cannon('b8', 'BLUE', ' BCn1 '),
                             'BlueCannon2': Cannon('h8', 'BLUE', ' BCn2 '),
                             'BlueSoldier1': Soldier('a7', 'BLUE', ' BSr1 ', -1),
                             'BlueSoldier2': Soldier('c7', 'BLUE', ' BSr2 ', -1),
                             'BlueSoldier3': Soldier('e7', 'BLUE', ' BSr3 ', -1),
                             'BlueSoldier4': Soldier('g7', 'BLUE', ' BSr4 ', -1),
                             'BlueSoldier5': Soldier('i7', 'BLUE', ' BSr5 ', -1)}

    def get_pieces(self):
        """
        Getter method for blue pieces dictionary
        :return: Dictionary containing piece objects of the blue player
        """
        return self._blue_pieces


class RedPlayer:
    """
    Represents the Red player
    """

    def __init__(self):
        """Initializes the red player's pieces"""
        self._red_pieces = {'RedGeneral': General('e2', 'RED', ' RGen ', 1),
                            'RedGuard1': Guard('d1', 'RED', ' RGd1 ', 1),
                            'RedGuard2': Guard('f1', 'RED', ' RGd2 ', 1),
                            'RedHorse1': Horse('c1', 'RED', ' RHs1 '),
                            'RedHorse2': Horse('h1', 'RED', ' RHs2 '),
                            'RedElephant1': Elephant('b1', 'RED', ' REl1 '),
                            'RedElephant2': Elephant('g1', 'RED', ' REl2 '),
                            'RedChariot1': Chariot('a1', 'RED', ' RCh1 '),
                            'RedChariot2': Chariot('i1', 'RED', ' RCh2 '),
                            'RedCannon1': Cannon('b3', 'RED', ' RCn1 '),
                            'RedCannon2': Cannon('h3', 'RED', ' RCn2 '),
                            'RedSoldier1': Soldier('a4', 'RED', ' RSr1 ', 1),
                            'RedSoldier2': Soldier('c4', 'RED', ' RSr2 ', 1),
                            'RedSoldier3': Soldier('e4', 'RED', ' RSr3 ', 1),
                            'RedSoldier4': Soldier('g4', 'RED', ' RSr4 ', 1),
                            'RedSoldier5': Soldier('i4', 'RED', ' RSr5 ', 1)}

    def get_pieces(self):
        """
        Getter method for red pieces dictionary
        :return: Dictionary containing piece objects of the red player
        """
        return self._red_pieces


class JanggiGame:
    """
    Represents the overall Janggi gameplay
    """

    def __init__(self):
        """
        Initializes the game of Janggi
        """
        self._game_state = 'UNFINISHED'
        self._current_player = 'BLUE'
        self._game_board = GameBoard()
        self._blue_player = BluePlayer()
        self._red_player = RedPlayer()
        self._letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

    def get_game_state(self):
        """
        Getter method for the current game state
        :return: 'UNFINISHED' - if the game is unfinished
                 'RED_WON' if the red player has won
                 'BLUE_WON' if the blue player has won
        """
        return self._game_state

    def set_game_state(self, new_state):
        """
        Setter method for the game state
        :param new_state: value for the new game state ('RED_WON' or 'BLUE_WON')
        """
        self._game_state = new_state

    def get_current_player(self):
        """
        Getter method for the current player
        :return: the current player
        """
        return self._current_player

    def set_current_player(self, next_player):
        """
        Setter method for the next player
        :param next_player: next player whose turn it is to make a move
        """
        self._current_player = next_player

    def get_game_board(self):
        """
        Getter method for the GameBoard object
        :return: the GameBoard object
        """
        return self._game_board

    def get_player_obj(self, player_color):
        """
        Getter method for the Player objects
        :param player_color: color of the player
        :return: the Player object corresponding to the player color
        """

        if player_color == 'BLUE':
            return self._blue_player
        elif player_color == 'RED':
            return self._red_player
        else:
            return False

    def get_letter_to_number(self):
        """
        Getter method for the letter to number conversions
        :return: dictionary of letter to number conversions
        """
        return self._letter_to_number

    def algebraic_to_cartesian(self, algebraic_location):
        """
        Converts the piece location in algebraic notation to cartesian coordinates
        :param algebraic_location: location in algebraic notation
        :return: the location in cartesian coordinates
        """
        pass

    def cartesian_to_algebraic(self, cartesian_location):
        """
        Converts the piece location in cartesian coordinates to algebraic notation
        :param cartesian_location: location in cartesian coordinates (list of row and column indices)
        :return: the location in algebraic notation
        """
        pass

    def moving_own_piece(self, from_location, player):
        """

        :param from_location:
        :param player:
        :return:
        """

        for each_piece in player.get_pieces():
            if player.get_pieces()[each_piece].get_location() == from_location:
                return True
        return False

    def capturing_own_piece(self, to_location, player):
        """

        :param to_location:
        :param player:
        :return:
        """
        for each_piece in player.get_pieces():
            if player.get_pieces()[each_piece].get_location() == to_location:
                return True
        return False

    def skipping_turn(self, from_location, to_location):
        """

        :param from_location:
        :param to_location:
        :return:
        """
        if from_location == to_location:
            return True
        else:
            return False

    def is_in_check(self, player):
        """
        Determines if the player is in check
        :param player: 'red' or 'blue' for player being assessed for a checkmate
        :return: True - if the player is in check
                 False - if the player is not in check
        """
        pass

    def checkmate_detected(self, player):
        """
        Determines if a checkmate state has been reached
        :param player: player to assess a checkmate for
        :return: True - if the player's general is checkmated
                 False - if the player's general has not been checkmated
        """
        pass

    def test_move(self, from_location, temp_to_location):
        """
        Temporarily moves a players piece to a new location so is_in_check can be called to assess if the move
        resulted in the general being put in or staying in check
        :param from_location: current location of the piece to move temporarily
        :param temp_to_location: location to temporarily move the piece to assess for a checked general
        :return: True - if the move has not resulted in the player's general being put in or remaining in check
                 False - if the move has resulted in the player's general being put in or remaining in check
        """
        pass

    def make_move(self, from_location, to_location):
        """
        Performs the move of the player's turn
        :param from_location: location to move from
        :param to_location: location to move to
        :return: False - if the move cannot be performed
                 True - if the indicated move is performed
        """

        #   If the game has already been won
        if self.get_game_state() != 'UNFINISHED':
            return False
        #   If the from_location does not have a current player's piece
        if not self.moving_own_piece(from_location, self.get_player_obj(self.get_current_player())):
            return False
        #   If the to_location has another of the current player's pieces
        if not self.skipping_turn(from_location, to_location) and \
                self.capturing_own_piece(to_location, self.get_player_obj(self.get_current_player())):
            return False

        if not self.skipping_turn(from_location, to_location):
            # If the indicated move is not legal due to movement rules of piece (valid_move method)

            #   If the indicated move is blocked by another piece (get spots to check from move_conditions - may rename)
            #       Use the cartesian to algebraic method
            #       Run through both players and see if they have a piece in those spots
            #           If they do, return false

        #   If the indicated move is not legal due to placing the player's general in check (test_move method)

        # Otherwise:
        #   Make the indicated move (w/in the Piece objects and on the game board)
        #   Remove any captured piece (by updating piece location of opponent to 'CAPTURED')
        #   Assess if the other player's piece is in check by any # of current pieces (via is_in_check method)
        #   Update the game state as necessary (by assessing for checkmate, as necessary, via checkmate_detected)
        #   Update whose turn it is
        #   Return True
        return True


JG = JanggiGame()
print(JG.get_game_state())
JG.get_game_board().print_game_board()
print(JG.make_move('a4', 'a7'))
