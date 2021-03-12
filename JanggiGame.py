# Author: Tessa Melli
# Date: 3/11/21
# Description: Defines a 2-player game of Janggi with an interactive make_move method


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

    def get_palace(self, directionality):
        """
        Getter method for cartesian coordinates of the board locations within the palace
        :param directionality: directionality of the pieces (1 for red and -1 for blue)
        :return: red palace locations - if the directionality is 1
                 blue palace locations - if the directionality is -1
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

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the General Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # Attempting to move guard out of the palace
        if to_cartesian not in self.get_palace(self.get_directionality()):
            return False

        # if in one of the corners or in the center position:
        if from_cartesian in self.get_palace(self.get_directionality())[0:5]:
            if not (abs(from_cartesian[0] - to_cartesian[0]) <= 1 and abs(from_cartesian[1] - to_cartesian[1]) <= 1):
                return False

        # if currently on one of the 4 side positions
        else:
            if not abs(from_cartesian[0] - to_cartesian[0]) + abs(from_cartesian[1] - to_cartesian[1]) == 1:
                return False

        # returning True as a default if other instances covered previously aren't met
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

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Guard Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # Trying to move guard out of the palace
        if to_cartesian not in self.get_palace(self.get_directionality()):
            return False

        # if in one of the corners or in the center position:
        if from_cartesian in self.get_palace(self.get_directionality())[0:5]:
            if not (abs(from_cartesian[0] - to_cartesian[0]) <= 1 and abs(from_cartesian[1] - to_cartesian[1]) <= 1):
                return False

        # if currently on one of the 4 side positions
        else:
            if not abs(from_cartesian[0] - to_cartesian[0]) + abs(from_cartesian[1] - to_cartesian[1]) == 1:
                return False

        # return True as a default if other conditions are not met
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
        self._intermediate_locations = []

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'HORSE'
        """
        return self._piece_type

    def get_intermediate_locations(self):
        """
        Getter method for intermediate locations
        :return: a list of coordinates of locations the Horse piece traverses during its move
        """
        return self._intermediate_locations

    def add_intermediate_location(self, new_location):
        """
        Setter method for intermediate locations
        :param new_location: intermediate location to add to the list of intermediate locations in a piece's path
        """
        self._intermediate_locations.append(new_location)

    def clear_intermediate_locations(self):
        """
        Resets the list of intermediate locations
        """
        self._intermediate_locations.clear()

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Horse Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # if the Horse is moving vertically
        if abs(from_cartesian[0] - to_cartesian[0]) == 2 and abs(from_cartesian[1] - to_cartesian[1]) == 1:
            self.add_intermediate_location([int((from_cartesian[0]+to_cartesian[0]) / 2), from_cartesian[1]])
            return True

        # if the Horse is moving horizontally
        elif abs(from_cartesian[1] - to_cartesian[1]) == 2 and abs(from_cartesian[0] - to_cartesian[0]) == 1:
            self.add_intermediate_location([from_cartesian[0], int((from_cartesian[1] + to_cartesian[1]) / 2)])
            return True

        # Return False in all other conditions
        else:
            return False


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
        self._intermediate_locations = []

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'ELEPHANT'
        """
        return self._piece_type

    def get_intermediate_locations(self):
        """
        Getter method for the intermediate locations
        :return: list of locations within the path of the Elephant's move
        """
        return self._intermediate_locations

    def add_intermediate_location(self, new_location):
        """
        Adds intermediate locations to a list of locations within the Elephant's movement path
        :param new_location: location within the Elephant's movement path to add to the intermediate location list
        """
        self._intermediate_locations.append(new_location)

    def clear_intermediate_locations(self):
        """
        Resets the list of intermediate locations
        """
        self._intermediate_locations.clear()

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Elephant Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """
        # if the Elephant is moving north
        if from_cartesian[0] - to_cartesian[0] == 3 and abs(from_cartesian[1] - to_cartesian[1]) == 2:
            self.add_intermediate_location([from_cartesian[0] - 1, from_cartesian[1]])
            self.add_intermediate_location([from_cartesian[0] - 2, int((from_cartesian[1] + to_cartesian[1]) / 2)])
            return True
        # if the Elephant piece is moving south
        elif (from_cartesian[0] - to_cartesian[0]) == -3 and abs(from_cartesian[1] - to_cartesian[1]) == 2:
            self.add_intermediate_location([from_cartesian[0] + 1, from_cartesian[1]])
            self.add_intermediate_location([from_cartesian[0] + 2, int((from_cartesian[1] + to_cartesian[1]) / 2)])
            return True
        # if the Elephant piece is moving West
        elif abs(from_cartesian[0] - to_cartesian[0]) == 2 and from_cartesian[1] - to_cartesian[1] == 3:
            self.add_intermediate_location([from_cartesian[0], from_cartesian[1] - 1])
            self.add_intermediate_location([int((from_cartesian[0] + to_cartesian[0]) / 2), from_cartesian[1] - 2])
            return True
        # if the Elephant piece is moving East
        elif abs(from_cartesian[0] - to_cartesian[0]) == 2 and from_cartesian[1] - to_cartesian[1] == -3:
            self.add_intermediate_location([from_cartesian[0], from_cartesian[1] + 1])
            self.add_intermediate_location([int((from_cartesian[0] + to_cartesian[0]) / 2), from_cartesian[1] + 2])
            return True
        # return False for all other conditions
        else:
            return False


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
        self._intermediate_locations = []

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'CHARIOT'
        """
        return self._piece_type

    def get_intermediate_locations(self):
        """
        Getter method for the intermediate locations
        :return: list of locations within the path of the Chariot's move
        """
        return self._intermediate_locations

    def add_intermediate_location(self, new_location):
        """
        Adds intermediate locations to a list of locations within the Chariot's movement path
        :param new_location: location within the Chariot's movement path to add to the intermediate location list
        """
        self._intermediate_locations.append(new_location)

    def clear_intermediate_locations(self):
        """
        Resets the list of intermediate locations
        """
        self._intermediate_locations.clear()

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Chariot Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # if moving in a straight line vertically
        if abs(from_cartesian[0] - to_cartesian[0]) > 0 and from_cartesian[1] - to_cartesian[1] == 0:
            # moving in the direction of decreasing rows
            if from_cartesian[0] > to_cartesian[0]:
                for horizontal_index in range(to_cartesian[0] + 1, from_cartesian[0]):
                    self.add_intermediate_location([horizontal_index, to_cartesian[1]])
            # moving in the direction of increasing rows
            else:
                for horizontal_index in range(from_cartesian[0] + 1, to_cartesian[0]):
                    self.add_intermediate_location([horizontal_index, to_cartesian[1]])
            return True

        # if moving in a straight line horizontally
        elif from_cartesian[0] - to_cartesian[0] == 0 and abs(from_cartesian[1] - to_cartesian[1]) > 0:
            # moving in order of decreasing columns
            if from_cartesian[1] > to_cartesian[1]:
                for vertical_index in range(to_cartesian[1] + 1, from_cartesian[1]):
                    self.add_intermediate_location([to_cartesian[0], vertical_index])
            # moving in order of increasing columns
            else:
                for vertical_index in range(from_cartesian[1] + 1, to_cartesian[1]):
                    self.add_intermediate_location([to_cartesian[0], vertical_index])
            return True

        # if moving from one of the corners or the center of one of the palaces
        elif from_cartesian in self.get_palace(1)[0:5] or from_cartesian in self.get_palace(-1)[0:5]:
            # trying to not move in a straight line from the palace to outside the palace
            if not (to_cartesian in self.get_palace(1) or to_cartesian in self.get_palace(-1)):
                return False
            # not moving along the diagonal line in the palace
            if abs(from_cartesian[0] - to_cartesian[0]) != abs(from_cartesian[1] - to_cartesian[1]):
                return False
            # if moving to opposite corner of the palace
            if abs(from_cartesian[0] - to_cartesian[0]) == 2:
                self.add_intermediate_location(
                    [int((from_cartesian[0] + to_cartesian[0]) / 2), (from_cartesian[1] + to_cartesian[1])])
        else:
            return False

        # return True for all other conditions
        return True


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
        self._intermediate_locations = []

    def get_piece_type(self):
        """
        Getter method for the piece type
        :return: 'CANNON'
        """
        return self._piece_type

    def get_intermediate_locations(self):
        """
        Getter method for the intermediate locations
        :return: list of locations within the path of the Cannon's move
        """
        return self._intermediate_locations

    def add_intermediate_location(self, new_location):
        """
        Adds intermediate locations to a list of locations within the Cannon's movement path
        :param new_location: location within the Cannon's movement path to add to the intermediate location list
        """
        self._intermediate_locations.append(new_location)

    def clear_intermediate_locations(self):
        """
        Resets the list of intermediate locations
        :return:
        """
        self._intermediate_locations.clear()

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Cannon Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # if moving in a straight line vertically
        if abs(from_cartesian[0] - to_cartesian[0]) > 0 and from_cartesian[1] - to_cartesian[1] == 0:
            # moving in the direction of decreasing rows
            if from_cartesian[0] > to_cartesian[0]:
                for row_index in range(to_cartesian[0] + 1, from_cartesian[0]):
                    self.add_intermediate_location([row_index, to_cartesian[1]])
            # moving in the direction of increasing rows
            else:
                for row_index in range(from_cartesian[0] + 1, to_cartesian[0]):
                    self.add_intermediate_location([row_index, to_cartesian[1]])
            return True
        # if moving in a straight line horizontally
        elif from_cartesian[0] - to_cartesian[0] == 0 and abs(from_cartesian[1] - to_cartesian[1]) > 0:
            # moving in order of decreasing columns
            if from_cartesian[1] > to_cartesian[1]:
                for column_index in range(to_cartesian[1] + 1, from_cartesian[1]):
                    self.add_intermediate_location([to_cartesian[0], column_index])
            # moving in order of increasing columns
            else:
                for column_index in range(from_cartesian[1] + 1, to_cartesian[1]):
                    self.add_intermediate_location([to_cartesian[0], column_index])
            return True
        # if moving from one of the corners or the center of one of the palaces
        elif from_cartesian in self.get_palace(1)[0:5] or from_cartesian in self.get_palace(-1)[0:5]:
            # trying to not move in a straight line from the palace to outside the palace
            if not (to_cartesian in self.get_palace(1) or to_cartesian in self.get_palace(-1)):
                return False
            # not moving along the diagonal line in the palace
            if abs(from_cartesian[0] - to_cartesian[0]) != abs(from_cartesian[1] - to_cartesian[1]):
                return False
            # if moving to opposite corner of the palace
            if abs(from_cartesian[0] - to_cartesian[0]) == 2:
                self.add_intermediate_location(
                    [int((from_cartesian[0] + to_cartesian[0]) / 2), (from_cartesian[1] + to_cartesian[1])])
        else:
            return False

        return True


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

    def meets_move_conditions(self, from_cartesian, to_cartesian):
        """
        Move conditions for the Soldier Piece
        :param from_cartesian: the initial location (converted from algebraic to cartesian coordinates)
        :param to_cartesian: the to-location (converted from algebraic to cartesian coordinates)
        :return: True - if the piece is being moved according to it's movement rules
                 False - if the proposed move violates its movement rules
        """

        # if moving horizontally
        if abs(from_cartesian[1] - to_cartesian[1]) > 1:
            return False
        # if moving vertically
        if not (to_cartesian[0] - from_cartesian[0] == 0 or
                self.get_directionality() * (to_cartesian[0] - from_cartesian[0]) == 1):
            return False

        # if in diagonals or center of palace:
        if from_cartesian in self.get_palace(1)[0:5] or from_cartesian in self.get_palace(-1)[0:5]:
            # add ability to go diagonally
            if abs(to_cartesian[0] - from_cartesian[0]) + abs(to_cartesian[1] - from_cartesian[1]) > 2:
                return False

        # if not:
        else:
            if abs(to_cartesian[0] - from_cartesian[0]) + abs(to_cartesian[1] - from_cartesian[1]) > 1:
                return False

        # return True for all other conditions
        return True


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
        self._blue_pieces = [General('e9', 'blue', ' BGen ', -1),
                             Guard('d10', 'blue', ' BGd1 ', -1),
                             Guard('f10', 'blue', ' BGd2 ', -1),
                             Horse('c10', 'blue', ' BHs1 '),
                             Horse('h10', 'blue', ' BHs2 '),
                             Elephant('b10', 'blue', ' BEl1 '),
                             Elephant('g10', 'blue', ' BEl2 '),
                             Chariot('a10', 'blue', ' BCh1 '),
                             Chariot('i10', 'blue', ' BCh2 '),
                             Cannon('b8', 'blue', ' BCn1 '),
                             Cannon('h8', 'blue', ' BCn2 '),
                             Soldier('a7', 'blue', ' BSr1 ', -1),
                             Soldier('c7', 'blue', ' BSr2 ', -1),
                             Soldier('e7', 'blue', ' BSr3 ', -1),
                             Soldier('g7', 'blue', ' BSr4 ', -1),
                             Soldier('i7', 'blue', ' BSr5 ', -1)]

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
        self._red_pieces = [General('e2', 'red', ' RGen ', 1),
                            Guard('d1', 'red', ' RGd1 ', 1),
                            Guard('f1', 'red', ' RGd2 ', 1),
                            Horse('c1', 'red', ' RHs1 '),
                            Horse('h1', 'red', ' RHs2 '),
                            Elephant('b1', 'red', ' REl1 '),
                            Elephant('g1', 'red', ' REl2 '),
                            Chariot('a1', 'red', ' RCh1 '),
                            Chariot('i1', 'red', ' RCh2 '),
                            Cannon('b3', 'red', ' RCn1 '),
                            Cannon('h3', 'red', ' RCn2 '),
                            Soldier('a4', 'red', ' RSr1 ', 1),
                            Soldier('c4', 'red', ' RSr2 ', 1),
                            Soldier('e4', 'red', ' RSr3 ', 1),
                            Soldier('g4', 'red', ' RSr4 ', 1),
                            Soldier('i4', 'red', ' RSr5 ', 1)]

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
        self._current_player = 'blue'
        self._current_piece = None
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

    def get_current_piece(self):
        """
        Getter method for the current piece
        :return: current piece attempting to make a move
        """
        return self._current_piece

    def set_current_piece(self, current_piece):
        """
        Setter method for the current piece
        :param current_piece: piece to set as the current
        """
        self._current_piece = current_piece

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

        if player_color == 'blue':
            return self._blue_player
        elif player_color == 'red':
            return self._red_player
        else:
            return False

    def get_opposite_player(self, player_color):
        """
        Getter method for the opposite player based on color
        :param player_color: player color fo the current player
        :return: Blue Player - if the current player color is 'red'
                 Red Player - if the current player color is 'blue'
        """
        if player_color == 'red':
            return self._blue_player
        elif player_color == 'blue':
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

        return [int(algebraic_location[1:]), self.get_letter_to_number()[algebraic_location[0]]]

    def cartesian_to_algebraic(self, cartesian_location):
        """
        Converts the piece location in cartesian coordinates to algebraic notation
        :param cartesian_location: location in cartesian coordinates (list of row and column indices)
        :return: the location in algebraic notation
        """

        column_letter = ''

        for item in self.get_letter_to_number():
            if self.get_letter_to_number()[item] == cartesian_location[1]:
                column_letter = item

        return column_letter + str(cartesian_location[0])

    def moving_own_piece(self, from_location, player):
        """
        Determines if the current player is moving their own piece
        :param from_location: start location of the piece
        :param player: current player
        :return: True - if the current player is moving their own piece
                 False - if the current player is not moving their own piece
        """

        for each_piece in player.get_pieces():
            if each_piece.get_location() == from_location:
                self.set_current_piece(each_piece)
                return True
        return False

    def skipping_turn(self, from_location, to_location):
        """
        Method to determine if the player is skipping their own turn (from_location and to_location are the same)
        :param from_location: starting location of the piece during the move
        :param to_location: ending location of the piece during the move
        :return: True - if the player is skipping their move
                 False - if the player is not skipping their move
        """
        if from_location == to_location:
            return True
        else:
            return False

    def capturing_own_piece(self, to_location, player):
        """
        Method to determine if a player is attempting to capture their own piece during a move
        :param to_location: ending location of piece during its move
        :param player: current player
        :return: True - if a player is attempting to make a move that results in a player capturing their own piece
                 False - if a player is not attempting to make a move that results in them capturing their own piece
        """
        for each_piece in player.get_pieces():
            if each_piece.get_location() == to_location:
                return True
        return False

    def move_is_blocked(self, current_piece):
        """
        Method to determine if the move is blocked by pieces in the current location
        :param current_piece: current piece being assessed for a block
        :return: True - if a piece is blocked due to other pieces in its movement path
                 False - if the piece is not being blocked by any other pieces in its movement path
        """

        # if the piece type is a 'HORSE', 'ELEPHANT', or 'CHARIOT'
        if (current_piece.get_piece_type() == 'HORSE' or
            current_piece.get_piece_type() == 'ELEPHANT' or
            current_piece.get_piece_type() == 'CHARIOT') and \
                len(current_piece.get_intermediate_locations()) != 0:
            # conditions for HORSE, ELEPHANT, or 'CHARIOT'
            print(current_piece.get_piece_type())
            print(current_piece.get_intermediate_locations())
            for intermediate_location in current_piece.get_intermediate_locations():
                for red_piece in self.get_player_obj('red').get_pieces():
                    if red_piece.get_location() == self.cartesian_to_algebraic(intermediate_location):
                        current_piece.clear_intermediate_locations()
                        return True
                for blue_piece in self.get_player_obj('blue').get_pieces():
                    if blue_piece.get_location() == self.cartesian_to_algebraic(intermediate_location):
                        current_piece.clear_intermediate_locations()
                        return True
            current_piece.clear_intermediate_locations()
            return False
        # if the piece type is a 'CANNON'
        elif current_piece.get_piece_type() == 'CANNON':
            if len(current_piece.get_intermediate_locations()) == 0:
                return True
            # conditions for 'CANNON'
            else:
                intermediate_pieces = 0
                for intermediate_location in current_piece.get_intermediate_locations():
                    for red_piece in self.get_player_obj('red').get_pieces():
                        if red_piece.get_location() == self.cartesian_to_algebraic(intermediate_location):
                            if red_piece.get_piece_type() == 'CANNON':
                                current_piece.clear_intermediate_locations()
                                return True
                            else:
                                intermediate_pieces += 1
                    for blue_piece in self.get_player_obj('blue').get_pieces():
                        if blue_piece.get_location() == self.cartesian_to_algebraic(intermediate_location):
                            if blue_piece.get_piece_type() == 'CANNON':
                                current_piece.clear_intermediate_locations()
                                return True
                            else:
                                intermediate_pieces += 1
                # only valid if the Cannon is jumping over a single piece (friend or Foe)
                if intermediate_pieces != 1:
                    current_piece.clear_intermediate_locations()
                    return True

                # return False for all other conditions
                else:
                    current_piece.clear_intermediate_locations()
                    return False

        # if the piece type is not an 'HORSE', 'ELEPHANT', 'CHARIOT', or 'CANNON'
        else:
            return False

    def cannon_capturing_cannon(self, current_piece, to_location):
        """
        Method to determine if a cannon piece is attempting to capture another cannon
        :param current_piece: current piece being assessed
        :param to_location: end location for a move of the cannon piece
        :return: True - if a player's Cannon piece is attempting to capture another Cannon
                 False - if not
        """
        if current_piece.get_piece_type() == 'CANNON':
            for blue_piece in self.get_player_obj('blue').get_pieces():
                if blue_piece.get_location() == to_location and blue_piece.get_piece_type() == 'CANNON':
                    return True
            for red_piece in self.get_player_obj('red').get_pieces():
                if red_piece.get_location() == to_location and red_piece.get_piece_type() == 'CANNON':
                    return True
        else:
            return False

    def is_in_check(self, player_color):
        """
        Determines if the player is in check
        :param player_color: 'red' or 'blue' for player being assessed for a checkmate
        :return: True - if the player is in check
                 False - if the player is not in check
        """

        # find location of player's general
        general_location = self.get_player_obj(player_color).get_pieces()[0].get_location()

        # for each of alternate player's pieces:
        for opponent_piece in self.get_opposite_player(player_color).get_pieces():
            if opponent_piece.get_location() != 'CAPTURED':
                if opponent_piece.meets_move_conditions(self.algebraic_to_cartesian(opponent_piece.get_location()),
                                                        self.algebraic_to_cartesian(general_location)):
                    if not self.move_is_blocked(opponent_piece):
                        return True
        return False

    def test_move(self, current_piece, from_location, temp_to_location):
        """
        Temporarily moves a players piece to a new location so is_in_check can be called to assess if the move
        resulted in the general being put in or staying in check
        :param from_location: current location of the piece to move temporarily
        :param temp_to_location: location to temporarily move the piece to assess for a checked general
        :return: True - if the move has not resulted in the player's general being put in or remaining in check
                 False - if the move has resulted in the player's general being put in or remaining in check
        """

        # if there's a player that will be captured, change their location to 'CAPTURED'
        other_piece = False

        # determining if other pieces would be captured as a result of this move
        if from_location != temp_to_location:
            for piece in self.get_player_obj('blue').get_pieces():
                if piece.get_location() == temp_to_location:
                    other_piece = True
                    opponent_piece = piece
                    piece.set_location('CAPTURED')

            for piece in self.get_player_obj('red').get_pieces():
                if piece.get_location() == temp_to_location:
                    other_piece = True
                    opponent_piece = piece
                    piece.set_location('CAPTURED')

        # change the current piece's location to the temp_to_location
        current_piece.set_location(temp_to_location)

        # assessing if the move puts the current player in check
        piece_color = current_piece.get_color()
        if self.is_in_check(piece_color):
            current_piece.set_location(from_location)
            if other_piece:
                opponent_piece.set_location(temp_to_location)
            return False
        else:
            current_piece.set_location(from_location)
            if other_piece:
                opponent_piece.set_location(temp_to_location)
            return True

    def valid_move(self, from_location, to_location):
        """
        Method to determine if a move is valid
        :param from_location: initial location of the piece
        :param to_location: final location of the piece
        :return: True - if the move is valid
                 False - if the move is not valid due to violating a condition
        """

        # If the from_location does not have a current player's piece
        if not self.moving_own_piece(from_location, self.get_player_obj(self.get_current_player())):
            return False

        # If the piece to be moved is captured:
        if self.get_current_piece().get_location() == 'CAPTURED':
            return False

        # If the to_location has another of the current player's pieces
        if not self.skipping_turn(from_location, to_location) and \
                self.capturing_own_piece(to_location, self.get_player_obj(self.get_current_player())):
            return False

        # If the player is not skipping their turn
        if not self.skipping_turn(from_location, to_location):

            # If the indicated move is not legal due to movement rules of piece
            if not self.get_current_piece().meets_move_conditions(self.algebraic_to_cartesian(from_location),
                                                                  self.algebraic_to_cartesian(to_location)):
                return False

            # if the move is blocked by another piece in the movement path
            if self.move_is_blocked(self.get_current_piece()):
                return False

            # if a cannon is attempting to capture another cannon
            if self.cannon_capturing_cannon(self.get_current_piece(), to_location):
                return False

        # return True for all other conditions
        return True

    def checkmate_detected(self, player):
        """
        Determines if a checkmate state has been reached
        :param player: player to assess a checkmate for
        :return: True - if the player's general is checkmated
                 False - if the player's general has not been checkmated
        """

        # Whoever is in check, run through each piece and try to move them to each position on the board
        for pieces in player.get_pieces():
            self.set_current_piece(pieces)
            for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
                for number in range(1, 11):
                    if self.valid_move(pieces.get_location(), letter + str(number)) and \
                            self.test_move(pieces, pieces.get_location(), letter + str(number)):
                        print(self.valid_move(pieces.get_location(), letter + str(number)))
                        print(self.test_move(pieces, pieces.get_location(), letter + str(number)))
                        print(pieces.get_nickname())
                        print(pieces.get_location())
                        print(letter + str(number))
                        return False
        return True

    def make_move(self, from_location, to_location):
        """
        Performs the move of the player's turn
        :param from_location: location to move from
        :param to_location: location to move to
        :return: False - if the move cannot be performed
                 True - if the indicated move is performed
        """

        print("Attempting: " + from_location + "->" + to_location)

        # If the game has already been won
        if self.get_game_state() != 'UNFINISHED':
            return False

        # If the move is not valid:
        if not self.valid_move(from_location, to_location):
            return False

        # if the test_move results in the player being put in check
        if not self.test_move(self.get_current_piece(), from_location, to_location):
            return False

        #   Make the indicated move
        self.get_current_piece().set_location(to_location)

        # Update the game board
        self.get_game_board().modify_game_board(self.algebraic_to_cartesian(from_location)[0],
                                                self.algebraic_to_cartesian(from_location)[1], '      ')
        self.get_game_board().modify_game_board(self.algebraic_to_cartesian(to_location)[0],
                                                self.algebraic_to_cartesian(to_location)[1],
                                                self.get_current_piece().get_nickname())

        # setting location for any captured pieces to 'CAPTURED'
        for other_pieces in self.get_opposite_player(self.get_current_player()).get_pieces():
            if other_pieces.get_location() == to_location:
                other_pieces.set_location('CAPTURED')

        # conditions if current player is blue
        if self.get_current_player() == 'blue':
            self.set_current_player('red')
            if self.is_in_check(self.get_current_player()):
                if self.checkmate_detected(self.get_player_obj(self.get_current_player())):
                    self.set_game_state('BLUE_WON')

        # conditions if current player is red
        else:
            self.set_current_player('blue')
            if self.is_in_check(self.get_current_player()):
                if self.checkmate_detected(self.get_player_obj(self.get_current_player())):
                    self.set_game_state('RED_WON')

        # return True for all other conditions
        return True
