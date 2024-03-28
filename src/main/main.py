from diceGameBuilder import DiceGameBuilder
from diceGameStateClass import DiceGameStateClass
from diceGameRulesClass import DiceGameRulesClass
from scorekeeperClass import ScorekeeperClass
from diceGame import DiceGame
from diceGameSimulator import DiceGameSimulator


diceGameSimulator = DiceGameSimulator(1000, 5, 6)
diceGameSimulator.simulate()

#builder = DiceGameBuilder()
#game_state = DiceGameStateClass(5, 6)
#game_rules = DiceGameRulesClass()
#scorekeeper = ScorekeeperClass()

#game: DiceGame = builder.withGameState(game_state).withGameRules(game_rules).withScorekeeper(scorekeeper).build()
#game.play()
#print(scorekeeper.getScores())
