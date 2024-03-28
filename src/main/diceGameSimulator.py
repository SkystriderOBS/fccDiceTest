from diceGameBuilder import DiceGameBuilder
from diceGameStateClass import DiceGameStateClass
from diceGameRulesClass import DiceGameRulesClass
from scorekeeperClass import ScorekeeperClass
from diceGame import DiceGame
import time

class DiceGameSimulator:
    
    #constructor for number of simulations
    def __init__(self, numSimulations: int, numDice: int, numSides: int):
        self.numSimulations = numSimulations
        self.numDice = numDice
        self.numSides = numSides

    def simulate(self):
        
        builder = DiceGameBuilder()
        game_rules = DiceGameRulesClass()
        scorekeeper = ScorekeeperClass()

        print("Number of simulations was " + str(self.numSimulations) +
              " using " + str(self.numDice) + " dice with " + str(self.numSides) + " sides.")
        
        start_time = time.time()
        
        for i in range(self.numSimulations):
            game_state = DiceGameStateClass(self.numDice, self.numSides)
            game: DiceGame = builder.withGameState(game_state).withGameRules(game_rules).withScorekeeper(scorekeeper).build()
            game.play()

        
        for score in scorekeeper.getScores():
            print(score)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Simulation took {:.4f} seconds".format(elapsed_time))
            
