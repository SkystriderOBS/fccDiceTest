#abstract class for dice game rules exposing methods for rolling dice that returns self and method that applies a set of rules to a dice game state
from abc import ABC, abstractmethod

class DiceGameRules(ABC):
    @abstractmethod
    def applyRules(self, gameState):
        """Apply the rules to the game state"""
        pass

    #isGameOver method that returns a boolean indicating if the game is over
    @abstractmethod
    def isGameOver(self, gameState):
        """Check if the game is over"""
        pass