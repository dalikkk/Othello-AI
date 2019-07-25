import random
class MyPlayer():
    '''Template Docstring for MyPlayer, look at the TODOs''' # TODO a short description of your player

    def __init__(self, my_color,opponent_color, board_size=8):
        self.name = 'username' #TODO: fill in your username
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board_size = board_size

    def move(self,board):
        possibilities = self.get_all_valid_moves(board)
        '''for j in possibilities:
            dx = [-1, -1, -1, 0, 1, 1, 1, 0]
            dy = [-1, 0, 1, 1, 1, 0, -1, -1]
            for i in range(len(dx)):
                print(self.__confirm_direction(j, dx[i], dy[i], board)[0])'''

        def up(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]-1][position[1]] == self.opponent_color:
                    changed = 1
                    while board[position[0]-1][position[1]] == self.opponent_color:
                        changed += 1
                        position[0] -= 1
                    if board[position[0]-1][position[1]] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def down(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]+1][position[1]] == self.opponent_color:
                    changed = 1
                    while board[position[0]+1][position[1]] == self.opponent_color:
                        changed += 1
                        position[0] += 1
                    if board[position[0]+1][position[1]] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def left(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]][position[1]-1] == self.opponent_color:
                    changed = 1
                    while board[position[0]][position[1]-1] == self.opponent_color:
                        changed += 1
                        position[1] -= 1
                    if board[position[0]][position[1]-1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def right(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]][position[1]+1] == self.opponent_color:
                    changed = 1
                    while board[position[0]][position[1]+1] == self.opponent_color:
                        changed += 1
                        position[1] += 1
                    if board[position[0]][position[1]+1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def diagonal_LU(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]-1][position[1]-1] == self.opponent_color:
                    changed = 1
                    while board[position[0]-1][position[1]-1] == self.opponent_color:
                        changed += 1
                        position[0] -= 1
                        position[1] += 1
                    if board[position[0]-1][position[1]-1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def diagonal_RU(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]-1][position[1]+1] == self.opponent_color:
                    changed = 1
                    while board[position[0]-1][position[1]+1] == self.opponent_color:
                        changed += 1
                        position[0] -= 1
                        position[1] += 1
                    if board[position[0]-1][position[1]+1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def diagonal_RD(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]+1][position[1]+1] == self.opponent_color:
                    changed = 1
                    while board[position[0]+1][position[1]+1] == self.opponent_color:
                        changed += 1
                        position[0] += 1
                        position[1] += 1
                    if board[position[0]+1][position[1]+1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        def diagonal_LD(position):
            changed = 0
            position = list(position)
            try:
                if board[position[0]+1][position[1]-1] == self.opponent_color:
                    changed = 1
                    while board[position[0]+1][position[1]-1] == self.opponent_color:
                        changed += 1
                        position[0] += 1
                        position[1] -= 1
                    if board[position[0]+1][position[1]-1] == self.my_color:
                        return changed
                    else:
                        return 0
                else:
                    return 0
            except:
                return 0

        print(possibilities, 'Vsetky moznosti.')

        maximum = [0, 0]
        for i in possibilities:
            print(i)
            print(up(i)+diagonal_RU(i)+right(i)+diagonal_RD(i)+down(i)+diagonal_LD(i)+left(i)+diagonal_LU(i))
            if up(i)+diagonal_RU(i)+right(i)+diagonal_RD(i)+down(i)+diagonal_LD(i)+left(i)+diagonal_LU(i) > maximum[0]:
                maximum[0] = up(i)+diagonal_RU(i)+right(i)+diagonal_RD(i)+down(i)+diagonal_LD(i)+left(i)+diagonal_LU(i)
                maximum[1] = i
        return maximum[1]
        # TODO: write you method
        # you can implement auxiliary fucntions, of course

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
    
