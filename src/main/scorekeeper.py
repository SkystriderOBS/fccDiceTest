#scorekeeper interface for the scorekeeperClass
from abc import ABC, abstractmethod

class ScoreKeeper(ABC):
    @abstractmethod
    def addScore(self, score):
        """Add a score to the scorekeeper"""
        pass
    @abstractmethod
    def getScore(self, score):
        """Get the number of times a score has been added"""
        pass
    @abstractmethod
    def getScores(self):
        """Get all the scores and the number of times they have been added"""
        pass