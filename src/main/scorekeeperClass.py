#Scorekeeper class that counts how many times a specific score occures
from typing import List
from scorekeeper import ScoreKeeper

class ScorekeeperClass(ScoreKeeper):
    def __init__(self):
        self.scores = {}
    def addScore(self, score: int):
        if score in self.scores:
            self.scores[score] += 1
        else:
            self.scores[score] = 1
    def getScore(self, score: int) -> int:
        if score in self.scores:
            return self.scores[score]
        else:
            return 0
        
    #write all the scores to a list of strings
    def getScores(self) -> List[int]:
        total = sum(self.scores.values())
        return ["Total {} occurs {:.2f}% occurred {} times".format(score, (self.scores[score]/total)*100, self.scores[score]) for score in sorted(self.scores)]


    