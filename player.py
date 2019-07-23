import random
from game_board import GameBoard


class MyGameBoard(GameBoard):
    def __init__(self, board):
        super().__init__()
        self.board = board


class MyPlayer:
    '''Template Docstring for MyPlayer, look at the TODOs''' # TODO a short description of your player

    def __init__(self, my_color, opponent_color, board_size=8):
        self.name = 'username' #TODO: fill in your username
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board_size = board_size

    def move(self, board):
        # TODO: write you method
        # you can implement auxiliary fucntions, of course
        my_board = MyGameBoard(board)
        print(my_board.board)
        result = self.go_through_minimax(my_board, 4)

        return result[1]

    #board.play_move()

    def go_through_minimax(self, board, plunging, ex=True):
        if plunging == 0:
            return self._evaluate_board(board, ex), None
        if ex:
            moves = self.get_all_valid_moves(board.board)
            if moves is None:
                return self.go_through_minimax(board, plunging - 1, False)
            best_result = None
            best_move = None
            for move in moves:
                my_board = MyGameBoard(board.get_board_copy())
                my_board.play_move(move, self.my_color)
                result = self.go_through_minimax(my_board, plunging - 1, False)[0]
                if best_result is None:
                    best_result = result
                    best_move = move
                if best_result < result:
                    best_result = result
                    best_move = move
            return best_result, best_move
        else:
            moves = self.get_all_valid_moves(board.board)
            if moves is None:
                return self.go_through_minimax(board, plunging - 1, True)
            worst_result = None
            worst_move = None
            for move in moves:
                my_board = MyGameBoard(board.get_board_copy())
                my_board.play_move(move, self.opponent_color)
                result = self.go_through_minimax(my_board, plunging - 1, True)[0]
                if worst_result is None:
                    worst_result = result
                    worst_move = move
                if worst_result > result:
                    worst_result = result
                    worst_move = move
            return worst_result, worst_move

    def _evaluate_board(self, board, ex):
        board = board.board
        exist_my_color = False
        exist_opponent_color = False
        exist_empty_color = False
        my_color_count = 0
        opponent_color_count = 0
        empty_color_count = 0
        for row in board:
            for cell in row:
                if cell == self.my_color:
                    exist_my_color = True
                    my_color_count += 1
                if cell == self.my_color:
                    exist_opponent_color = True
                    opponent_color_count += 1
                if cell == -1:
                    exist_empty_color = True
                    empty_color_count += 1
        if exist_my_color is False:
            return -1

        if exist_opponent_color is False:
            return 2

        if exist_empty_color is False:
            if my_color_count > opponent_color_count:
                return 2
            else:
                return -1

        my_score = 200
        opponent_score = 200
        vertexes = [(0, 0), (7, 0), (0, 7), (7, 7)]
        for move in vertexes:
            if board[move[0]][move[1]] == self.my_color:
                my_score += 100
            if board[move[0]][move[1]] == self.opponent_color:
                opponent_score += 100

        dangers = [(1, 1), (6, 1), (1, 6), (6, 6)]
        for i in range(len(dangers)):
            move = dangers[i]
            vertex = vertexes[i]
            if board[move[0]][move[1]] == self.my_color and board[vertex[0]][vertex[1]] == -1:
                my_score -= 50
            if board[move[0]][move[1]] == self.opponent_color and board[vertex[0]][vertex[1]] == -1:
                opponent_score -= 50

        edges = [(0, 2), (0, 3), (0, 4), (0, 5),
                 (2, 7), (3, 7), (4, 7), (5, 7),
                 (7, 5), (7, 4), (7, 3), (7, 2)]
        for move in edges:
            if board[move[0]][move[1]] == self.my_color:
                my_score += 10
            if board[move[0]][move[1]] == self.opponent_color:
                opponent_score += 10

        dangerous_edges = [(0, 1), (1, 0), (0, 6), (1, 7), (6, 7), (7, 6), (7, 1), (6, 0)]
        if empty_color_count > 10:
            for move in dangerous_edges:
                if board[move[0]][move[1]] == self.my_color:
                    my_score -= 10
                if board[move[0]][move[1]] == self.opponent_color:
                    opponent_score -= 10

        edges_making_positions = [(1, 2), (1, 3), (1, 4), (1, 5),
                                  (2, 6), (3, 6), (4, 6), (5, 6),
                                  (6, 5), (6, 4), (6, 4), (6, 2),
                                  (5, 1), (4, 1), (3, 1), (2, 1)]

        for move in edges_making_positions:
            if board[move[0]][move[1]] == self.my_color:
                if empty_color_count > 25:
                    my_score -= 2
                else:
                    my_score -= 1
            if board[move[0]][move[1]] == self.opponent_color:
                if empty_color_count > 25:
                    opponent_score -= 2
                else:
                    opponent_score -= 1

        starting_good_pos = [(2, 2), (2, 6), (6, 2), (6, 6)]
        for move in starting_good_pos:
            if board[move[0]][move[1]] == self.my_color:
                if empty_color_count > 20:
                    my_score += 5
            if board[move[0]][move[1]] == self.opponent_color:
                if empty_color_count > 20:
                    opponent_score += 5

        unimportant_positions = []
        for i in range(2, 6):
            for j in range(2, 6):
                unimportant_positions.append((i, j))

        for move in unimportant_positions:
            if board[move[0]][move[1]] == self.my_color:
                if empty_color_count < 20:
                    my_score += 2
            if board[move[0]][move[1]] == self.opponent_color:
                if empty_color_count < 20:
                    opponent_score += 2

        # sumarise score
        if my_score < 0:
            my_score = 0

        if opponent_score < 0:
            opponent_score = 0

        if my_score == 0 and opponent_score == 0:
            return 0.5

        return my_score / (my_score + opponent_score)


    """
    def clone_board(self, board):
        pass

    def invert_board(self, board):
        my_board = self.clone_board(board)
        for row in my_board:
            for i in range(len(row)):
                if row[i] == self.my_color:
                    row[i] = self.opponent_color
                elif row[i] == self.opponent_color:
                    row[i] == self.my_color
        return my_board
    """

    def __is_correct_move(self, move, board):
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(len(dx)):
            if self.__confirm_direction(move, dx[i], dy[i], board)[0]:
                return True, 
        return False

    def __confirm_direction(self, move, dx, dy, board):
        posx = move[0]+dx
        posy = move[1]+dy
        opp_stones_inverted = 0
        if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
            if board[posx][posy] == self.opponent_color:
                opp_stones_inverted += 1
                while (posx >= 0) and (posx <= (self.board_size-1)) and (posy >= 0) and (posy <= (self.board_size-1)):
                    posx += dx
                    posy += dy
                    if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                        if board[posx][posy] == -1:
                            return False, 0
                        if board[posx][posy] == self.my_color:
                            return True, opp_stones_inverted
                    opp_stones_inverted += 1

        return False, 0

    def get_all_valid_moves(self, board):
        valid_moves = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                if (board[x][y] == -1) and self.__is_correct_move([x, y], board):
                    valid_moves.append( (x, y) )

        if len(valid_moves) <= 0:
            print('No possible move!')
            return None
        return valid_moves
    
