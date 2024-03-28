from diceGameStateClass import DiceGameStateClass
from diceGameRulesClass import DiceGameRulesClass
from scorekeeperClass import ScorekeeperClass
from diceGame import DiceGame

class DiceGameBuilder:
    def __init__(self):
        self.gameState = None
        self.gameRules = None
        self.scorekeeper = None

    def withGameState(self, gameState: DiceGameStateClass):
        if not isinstance(gameState, DiceGameStateClass):
            raise TypeError("gameState must be an instance of DiceGameStateClass")
        self.gameState = gameState
        return self

    def withGameRules(self, gameRules: DiceGameRulesClass):
        if not isinstance(gameRules, DiceGameRulesClass):
            raise TypeError("gameRules must be an instance of DiceGameRulesClass")
        self.gameRules = gameRules
        return self

    def withScorekeeper(self, scorekeeper: ScorekeeperClass):
        if not isinstance(scorekeeper, ScorekeeperClass):
            raise TypeError("scorekeeper must be an instance of ScorekeeperClass")
        self.scorekeeper = scorekeeper
        return self

    def build(self):
        if self.gameState is None or self.gameRules is None or self.scorekeeper is None:
            raise Exception("Missing component(s) to build DiceGame")
        return DiceGame(self.gameState, self.gameRules, self.scorekeeper)