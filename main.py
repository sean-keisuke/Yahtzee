from Roll import Roll
from ScoreCard import ScoreCard

class main:
	
	def printScoreCard(player):
		print("\nScoreCard for player " + str(player.getIndex()) +  ":\n")
		print("Aces:\t\t" + str(player.getOnes()))
		print("Twos:\t\t" + str(player.getTwos()))
		print("Threes:\t\t" + str(player.getThrees()))
		print("Fours:\t\t" + str(player.getFours()))
		print("Fives:\t\t" + str(player.getFives()))
		print("Sixes:\t\t" + str(player.getSixes()))

		if player.getUpperBonus:
			print("Upper Bonus:\t0")
		else:
			print("Upper Bonus:\t35")

		print("Upper Total:\t" + str(player.addUpper()))
		print("\n3 of a kind:\t" + str(player.getSetOfThree()))
		print("4 of a kind:\t" + str(player.getSetOfFour()))
		print("Full House:\t" + str(player.getFullHouse()))
		print("Small Straight:\t" + str(player.getSmallStraight()))
		print("Large Straight:\t" + str(player.getLargeStraight()))
		print("Yahtzee:\t" + str(player.getYahtzee()))
		print("\nTotal Score:\t" + str(player.totalScore()) + "\n")
	
	player1 = ScoreCard(1)
	printScoreCard(player1)
