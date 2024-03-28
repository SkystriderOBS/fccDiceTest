#abstract class for dice game state with number of dice, number of sides, and a list of dice and an integer score
from abc import ABC, abstractmethod

class DiceGameState(ABC):
    def __init__(self, numDice: int, numSides: int):
        self.numDice = numDice
        self.numSides = numSides
        self.dice = [0] * numDice
        self.score = 0
    @abstractmethod
    def rollDice(self):
        """Roll all the dice"""
        pass
    @abstractmethod
    def getScore(self):
        """Get the score"""
        pass
    @abstractmethod
    def getDice(self):
        """Get the dice"""
        pass
    @abstractmethod
    def setScore(self, score):
        """Set the score"""
        pass
    @abstractmethod
    def setDice(self, dice):
        """Set the dice"""
        pass
    @abstractmethod
    def setNumDice(self, numDice):
        """Set the number of dice"""
        pass
    @abstractmethod
    def setNumSides(self, numSides):
        """Set the number of sides"""
        pass
    @abstractmethod
    def getNumDice(self):
        """Get the number of dice"""
        pass
    @abstractmethod
    def getNumSides(self):
        """Get the number of sides"""
        pass