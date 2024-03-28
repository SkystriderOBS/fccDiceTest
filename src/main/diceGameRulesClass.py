#DiceGameRulesClass extending diceGameRules for a specific dice game with a private rule method that applies the rules to the game state
from diceGameRules import DiceGameRules
from diceGameState import DiceGameState

class DiceGameRulesClass(DiceGameRules):

    #public method that applies a set of rules to a dice game state
    def applyRules(self, gameState: DiceGameState):
        notDoneRoll = True
        notDoneRoll = notDoneRoll and self._applyRule1(gameState)
        notDoneRoll = notDoneRoll and self._applyRule2(gameState)
        return notDoneRoll
    
    #private
    def _applyRule1(self, gameState: DiceGameState) -> bool:
        #if there are any 3's in the dice, set the score to 0 and remove the 3's from the dice
        if 3 in gameState.getDice():
            # no value added to the score
            gameState.setDice([x for x in gameState.getDice() if x != 3])
            return False
        return True
    
    #private
    def _applyRule2(self, gameState: DiceGameState):
        #if there are no 3's in the dice, remove the lowest value die from the dice and add it to the score
        if 3 not in gameState.getDice():
            lowest = min(gameState.getDice())
            gameState.setScore(gameState.getScore() + lowest)
            gameState.setDice([x for x in gameState.getDice() if x != lowest])
            return False
        return True
    
    #isGameOver method that returns a boolean indicating if the game is over
    def isGameOver(self, gameState: DiceGameState) -> bool:
        return len(gameState.getDice()) == 0