from diceGameStateClass import DiceGameStateClass
from diceGameRulesClass import DiceGameRulesClass
from scorekeeperClass import ScorekeeperClass

class DiceGame:
    def __init__(self, gameState: DiceGameStateClass, gameRules: DiceGameRulesClass, scorekeeper: ScorekeeperClass):
        self.gameState = gameState
        self.gameRules = gameRules
        self.scorekeeper = scorekeeper

    def play(self):
        while not self.gameRules.isGameOver(self.gameState):
            self.gameState.rollDice()
            self.gameRules.applyRules(self.gameState)
        
        self.scorekeeper.addScore(self.gameState.getScore())