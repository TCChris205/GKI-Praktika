import random

class Countries:
    
    def __init__(self, maxColors = 5):
        self.map = staticDictionary()
        self.maxColors = maxColors

        # Random Colors
        self.colors = []
        for _ in range(len(self.map.keys())):
            self.colors.append(random.randint(0, maxColors-1))
    
    def mutation(self):
        self.colors[random.randint(0, len(self.map.keys())-1)] = random.randint(0, self.maxColors-1)

    def fitness(self):
        fitnessVal = 10 # Starting Value

        # Amount of Colors
        colorset = set()
        for c in self.colors:
            colorset.add(c)

        fitnessVal -= len(colorset)

        for country, adjacent in self.map.items():
            for a in adjacent:
                if self.colors[country] == self.colors[a]:
                    fitnessVal -= 1
        
        return fitnessVal

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
    child1 = Countries()
    child2 = Countries()

    swapBits = random.randint(1, 62)
    # Swapping
    # Generate Number between 1 and 62, Get the set bits. Swap Countries where set Bit = index. 0 and 63 excluded due to full swap. 

    # 32
    if swapBits % 32 == 1:
        swapBits -= 32
        child1.colors[0] = parent2.colors[0]
        child2.colors[0] = parent1.colors[0]
    else:
        child1.colors[0] = parent1.colors[0]
        child2.colors[0] = parent2.colors[0]
    
    # 16
    if swapBits % 16 == 1:
        swapBits -= 16
        child1.colors[1] = parent2.colors[1]
        child2.colors[1] = parent1.colors[1]
    else:
        child1.colors[1] = parent1.colors[1]
        child2.colors[1] = parent2.colors[1]
    
    # 8
    if swapBits % 8 == 1:
        swapBits -= 8
        child1.colors[2] = parent2.colors[2]
        child2.colors[2] = parent1.colors[2]
    else:
        child1.colors[2] = parent1.colors[2]
        child2.colors[2] = parent2.colors[2]
    
    # 4
    if swapBits % 4 == 1:
        swapBits -= 4
        child1.colors[3] = parent2.colors[3]
        child2.colors[3] = parent1.colors[3]
    else:
        child1.colors[3] = parent1.colors[3]
        child2.colors[3] = parent2.colors[3]

    # 2
    if swapBits % 2 == 1:
        swapBits -= 2
        child1.colors[4] = parent2.colors[4]
        child2.colors[4] = parent1.colors[4]
    else:
        child1.colors[4] = parent1.colors[4]
        child2.colors[4] = parent2.colors[4]

    # 1
    if swapBits % 1 == 1:
        swapBits -= 1
        child1.colors[5] = parent2.colors[5]
        child2.colors[5] = parent1.colors[5]
    else:
        child1.colors[5] = parent1.colors[5]
        child2.colors[5] = parent2.colors[5]

    return child1, child2

def sortByFitness(countries):
    return countries.fitness()

def staticDictionary():
    countriesDict = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3],
        5: []
    }
    return countriesDict

def run():
    # Sizes
    maxGenerations = 100
    population = 10 # Must be even, else the population will vary
    tournamentSize = 3 # Must be smaller than population
    optimalFitness = 7

    # Probabilities
    crossoverProb = 0.6
    mutationProb = 0.1

    # Stats
    generations = 0

    # Algorithm

    # Initialization
    currGeneration = [Countries() for _ in range(population)]

    # Loop
    for _ in range(maxGenerations):
        
        # Finishing Condition
        for c in currGeneration:
            if c.fitness() >= optimalFitness:
                # Print values
                print(f"Colors: {c.colors}")
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
        for c in nextGen:
            if random.randint(1, 10) <= mutationProb*10:
                c.mutation()

        generations += 1
        currGeneration = nextGen
    
    print(f"No solution found. Generations: {generations}")
    return -1

if __name__ == "__main__":
    results = [run() for _ in range(100)]
    print(results)