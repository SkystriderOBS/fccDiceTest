#class extending DiceGameState for a specific dice game
import random
from diceGameState import DiceGameState

class DiceGameStateClass(DiceGameState):
    def __init__(self, numDice: int, numSides: int):
        super().__init__(numDice, numSides)
    def rollDice(self):
        self.dice = [random.randint(1, self.numSides) for i in range(self.numDice)]
    def getScore(self):
        return self.score
    def getDice(self):
        return self.dice
    def setScore(self, score):
        self.score = score
    def setDice(self, dice):
        self.dice = dice
    def setNumDice(self, numDice):
        self.numDice = numDice
    def setNumSides(self, numSides):
        self.numSides = numSides
    def getNumDice(self):
        return self.numDice
    def getNumSides(self):
        return self.numSides