import random

class Queens:
    
    def __init__(self):
        # Generate Board
        self.board = [[0]*8 for _ in range(8)]

        # Create Queens
        for _ in range(8):
            while 1:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if self.board[x][y] == 0:
                    self.board[x][y] = 1
                    break
    
    def mutation(self):
        self.removeQueen()
        self.addQueen()

    def fitness(self):
        fitnessVal = 8 # Starting and Optimal Value

        # Get all Queens
        queenlist, count = self.queencount()
        
        # Count amount of Queens
        if not count == 8:
            fitnessVal = 0

        # Get all covered fields
        checkingBoard = [[0]*8 for _ in range(8)]

        for x, y in queenlist:
            resetQueenfield = True
            if checkingBoard[x][y] == 1:
                resetQueenfield = False

            for j in range(len(checkingBoard[x])):
                checkingBoard[x][j] = 1
            
            for i in range(len(checkingBoard)):
                checkingBoard[i][y] = 1

            # Reset Field of Queen
            if resetQueenfield:
                checkingBoard[x][y] = 0   
        
        # Check if any Queens are on occupied fields
        for x, y in queenlist:
            if checkingBoard[x][y] == 1:
                fitnessVal -= 1
        
        return fitnessVal
    
    def queencount(self):
        # Get all Queens
        queenlist = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    queenlist.append((i,j))
        
        return queenlist, len(queenlist)

    def addQueen(self):
        # Add a queen randomly
        while 1:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if self.board[x][y] == 0:
                self.board[x][y] = 1
                break

    def removeQueen(self):
        queenlist, count = self.queencount()
        x, y = queenlist[random.randint(1, count)-1]
        self.board[x][y] = 0

def selection(currGeneration, population, tournamentSize):
    matingPool = []
    for _ in range(population): # Number of Tournaments
            tournament = []

            for _ in range(tournamentSize):
                tournament.append(currGeneration[random.randint(1, len(currGeneration))-1])
            
            tournament.sort(key=sortByFitness)
            matingPool.append(tournament.pop())
    return matingPool

def crossover(parent1, parent2):
    swapInd = random.randint(1, 6)

    child1 = Queens()
    child2 = Queens()

    # Swapping
    child1.board = [r for r in parent1.board[:swapInd]] + [r for r in parent2.board[swapInd:]]
    child1.board = [r for r in parent2.board[:swapInd]] + [r for r in parent1.board[swapInd:]]

    # Adjusting number of Queens
    _, count1 = child1.queencount()
    while count1 < 8:
        child1.addQueen()
        count1 += 1
    while count1 > 8:
        child1.removeQueen()
        count1 -= 1

    _, count2 = child2.queencount()
    while count2 < 8:
        child2.addQueen()
        count2 += 1
    while count2 > 8:
        child2.removeQueen()
        count2 -= 1

    return child1, child2

def sortByFitness(queens):
    return queens.fitness()

def run():
    # Sizes
    maxGenerations = 100
    population = 100 # Must be even, else the population will vary
    tournamentSize = 10 # Must be smaller than population
    optimalFitness = 8

    # Probabilities
    crossoverProb = 0.6
    mutationProb = 0.1

    # Stats
    generations = 0

    # Algorithm

    # Initialization
    currGeneration = [Queens() for _ in range(population)]

    # Loop
    for _ in range(maxGenerations):
        
        # Finishing Condition
        for q in currGeneration:
            if q.fitness() >= optimalFitness:
                # Print values
                print(q.board)
                print(f"Generations: {generations}")
                return generations

        # Selection
        matingPool = selection(currGeneration, population, tournamentSize)
        
        # Crossover
        nextGen = []
        for _ in range(population//2):
            parent1 = matingPool[random.randint(1, len(matingPool))-1]
            parent2 = matingPool[random.randint(1, len(matingPool))-1]

            if random.randint(1, 10) <= crossoverProb*10:
                child1, child2 = crossover(parent1, parent2)
                nextGen.append(child1)
                nextGen.append(child2)
            else:
                nextGen.append(parent1)
                nextGen.append(parent2)

        # Mutation
        for q in nextGen:
            if random.randint(1, 10) <= mutationProb*10:
                q.mutation()

        generations += 1
        currGeneration = nextGen
    
    print(f"No solution found. Generations: {generations}")
    return -1

if __name__ == "__main__":
    results = [run() for _ in range(100)]
    print(results)