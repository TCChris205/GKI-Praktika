from math import inf
import numpy as np

count = 0

class Board:
    def __init__(self, movesX = np.array([]), movesO = np.array([])):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.movesX = movesX
        self.movesO = movesO
        for x in self.movesX:
            self.board[int(x)] = 1

        for o in self.movesO:
            self.board[int(o)] = 2

    def moveO(self, coordinate):
        if not coordinate in list(self.movesO) + list(self.movesX):
            moveO = np.append(self.movesO.copy(), [coordinate])
            return Board(self.movesX.copy(), moveO)
        return False

    def moveX(self, coordinate):
        if not coordinate in list(self.movesO) + list(self.movesX):
            moveX = np.append(self.movesX.copy(), [coordinate])
            return Board(moveX, self.movesO.copy())
        return False
    
    def utility(self):
        # Horizontal
        for i in range(0,3):
            if self.board[0 + 3*i] == self.board[1 + 3*i] == self.board[2 + 3*i] != 0:
                if self.board[0 + 3*i] == 1:
                    return 1
                return -1

        # Vertical
        for i in range(0,3):
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] != 0:
                if self.board[0 + i] == 1:
                    return 1
                return -1

        # Diagonal
        if self.board[0] == self.board[4] == self.board[8] != 0:
            if self.board[0] == 1:
                return 1
            return -1

        if self.board[2] == self.board[4] == self.board[6] != 0:
            if self.board[2] == 1:
                return 1
            return -1
        
        return 0

    def terminal(self):
        if not self.utility() == 0:
            return True

        if all(self.board):
            return True

        return False

class State:
    def __init__(self, board, min = False):
        self.minToMove = min
        self.board = board
        self.children = []

    def terminal(self):
        return self.board.terminal()

    def utility(self):
        return self.board.utility()
    
def MaxValue(state, alpha, beta):
    global count
    count += 1
    if state.terminal(): 
        return state.utility(), state.board

    v = -inf
    a = None

    for m in range(9):
        new = state.board.moveX(m)
        if new:
            u, b = MaxValue(State(new, True), alpha, beta)
            if v < u:
                v = u
                a = b

            if v >= beta: return v, a
            alpha = max(alpha, v)
        
    return v, a


def MinValue(state, alpha, beta):
    global count
    count += 1
    if state.terminal(): 
        return state.utility(), state.board

    v = +inf
    a = None

    for m in range(9):
        new = state.board.moveO(m)
        if new:
            u, b = MaxValue(State(new, False), alpha, beta)
            if v > u:
                v = u
                a = b

            if v <= alpha: return v, a
            beta = min(beta, v)
    return v, a

def buildTree(state):
    buildChildren = []

    if state.minToMove: # O to move
        for m in range(9):
            new = state.board.moveO(m)
            if new:
                buildChildren.append(State(new, False))
    else: # X to move
        for m in range(9):
            new = state.board.moveX(m)
            if new:
                buildChildren.append(State(new, True))

    state.children = buildChildren

    for c in buildChildren:
        if not c.terminal():
            buildTree(c)

def run():
    start = State(Board())
    # print("Building Tree...")
    # buildTree(start)
    # print("Tree Build, Starting Calculations...")

    utility, board = MaxValue(start, -inf, inf)

    if utility == 1:
        print(f"Max Wins. Moves = {board.movesX}. Visited States: {count}")
    elif utility == -1:
        print(f"Min Wins. Moves = {board.movesO}. Visited States: {count}")
    else:
        print(f"Tie. Visited States: {count}")

if __name__ == "__main__":
    run()
