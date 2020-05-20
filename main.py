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
	
	def makeDecision(player, currentHand, helper):
		#time to add scores on the scorecard
		valid = 0
		while valid != 1:
			decision = raw_input("which row would you like to fill? \nFor list of acceptable keywords, type 'help'\n")
			if "aces" in decision.lower():
    				if player.getOnes == 0:
					player.setOnes(helper.upperScore(currentHand,1))
					valid = 1
			elif "twos" in decision.lower():
    				if player.getTwos == 0:
    					player.setTwos(helper.upperScore(currentHand,2))
					valid = 1
			elif "threes" in decision.lower():
    	    			if player.getThrees == 0:
					player.setThrees(helper.upperScore(currentHand,3))
					valid = 1
			elif "fours" in decision.lower():
				if player.getFours == 0:
    					player.setFours(helper.upperScore(currentHand,4))
					valid = 1
			elif "fives" in decision.lower():
    				if player.getFives == 0:
					player.setFives(helper.upperScore(currentHand,5))
					valid = 1
			elif "sixes" in decision.lower():
    				if player.getSixes == 0:
		    			player.setSixes(helper.upperScore(currentHand,6))
					valid = 1
			elif "3 of a kind" in decision.lower():
    				if player.getThreeOfKind == 0 and helper.threeOfKind(currentHand):
	    				player.setSetOfThree(helper.chance(currentHand))
					valid = 1
			elif "4 of a kind" in decision.lower():
    				if player.getFourOfKind == 0 and helper.FourOfKind(currentHand):
	    				player.setSetOfFour(helper.chance(currentHand))
					valid = 1
			elif "full house" in decision.lower():
    				if player.getFullHouse == 0 and helper.fullHouse(currentHand):
	    				player.setFullHouse()
					valid = 1
			elif "small straight" in decision.lower():
   				if player.getSmallStraight == 0 and helper.smallStraight(currentHand):
	    				player.setSmallStraight()
					valid = 1
			elif "large straight" in decision.lower():
   				if player.getLargeStraight == 0 and helper.largeStraight(currentHand):
	    				player.setLargeStraight()
					valid = 1
			elif "chance" in decision.lower():
				if player.getChance == 0:
					player.setChance(helper.chance(currentHand))
					valid = 1
			elif "help" in decision.lower():
				print("Acceptable keywords:\n aces, twos, threes, fours, fives, sixes")
				print("3 of a kind, 4 of a kind, full house, small straight, large straight, chance, yahtzee")
			elif "yahtzee" in decision.lower():
				if player.getnumOfYahtzee == 0:
					player.setYahtzee()
					valid = 1
				elif player.getnumOfYahtzee == 1:
					print("JOKER!! Select another Row to be filled also")
					makeDecision(player, currentHand, helper) #call function again
					player.setYahtzee()
					valid = 1
			else:
				print("Please enter a valid row")			

	
	rounds = 13 # number of rounds per game
	dice = Roll()	

	player1 = ScoreCard(1)

	for x in range(rounds):
		printScoreCard(player1)
		for y in range(3):
			dice.diceRoll() #roll the dice
			decision = raw_input("Reroll or Score?")
			if "score" in decision.lower():
				break

			dice.diceToKeep() #select which dice to keep

		decisionHand = dice.lastTurn #get list of current dices
		makeDecision(player1, decisionHand, dice)	
