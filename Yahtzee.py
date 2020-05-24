'''
Sean Mullarkey
Yahtzee Simulation
'''

from Roll import Roll
from ScoreCard import ScoreCard

class Yahtzee:
	
	def printScoreCard(player):

		print("\nScoreCard for " + str(player.getName()) +  ":\n")
		print("Aces:\t\t" + str(player.getOnes()))
		print("Twos:\t\t" + str(player.getTwos()))
		print("Threes:\t\t" + str(player.getThrees()))
		print("Fours:\t\t" + str(player.getFours()))
		print("Fives:\t\t" + str(player.getFives()))
		print("Sixes:\t\t" + str(player.getSixes()))

		if not player.getUpperBonus():
			print("Upper Bonus:\t0")
		else:
			print("Upper Bonus:\t35")

		print("Upper Total:\t" + str(player.addUpper()))
		print("\n3 of a kind:\t" + str(player.getSetOfThree()))
		print("4 of a kind:\t" + str(player.getSetOfFour()))
		print("Full House:\t" + str(player.getFullHouse()))
		print("Small Straight:\t" + str(player.getSmallStraight()))
		print("Large Straight:\t" + str(player.getLargeStraight()))
		print("Chance:\t\t" + str(player.getChance()))
		print("Yahtzee:\t" + str(player.getYahtzee()))
		print("\nTotal Score:\t" + str(player.totalScore()) + "\n")
	


	def makeDecision(player, currentHand, helper):
		#time to add scores on the scorecard
		valid = 0		
		def giveScoreUp(category): #I think this is gross. change later
			valid = 0
			while valid != 1:
				decision = raw_input("forfeit " + category + "? Enter Yes or No\n")
				if "yes" in decision.lower():
					return True
				else:
					return False
			return False

		while valid != 1:
			decision = raw_input("which row would you like to fill? \nFor list of possible moves, type 'help'\n")
			if "aces" in decision.lower():
	    			if "aces" in player.getDecisionList(): #if possible move
		    			if 1 not in currentHand:
						if giveScoreUp("Aces") == True:
							player.setOnes(helper.upperScore(currentHand,1))
							player.removeDecision("aces")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					else:
						player.setOnes(helper.upperScore(currentHand,1))
						player.removeDecision("aces")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "twos" in decision.lower():
				if "twos" in player.getDecisionList():
		    			if 2 not in currentHand:
						if giveScoreUp("Twos") == True:
							player.setTwos(helper.upperScore(currentHand,2))
							player.removeDecision("twos")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
    					else:
						player.setTwos(helper.upperScore(currentHand,2))
						player.removeDecision("twos")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "threes" in decision.lower():
				if "threes" in player.getDecisionList():
		    			if 3 not in currentHand:
						if giveScoreUp("Threes") == True:
							player.setThrees(helper.upperScore(currentHand,3))
							player.removeDecision("threes")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					else:
						player.setThrees(helper.upperScore(currentHand,3))
						player.removeDecision("threes")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "fours" in decision.lower():
				if "fours" in player.getDecisionList():
		    			if 4 not in currentHand:
						if giveScoreUp("Fours") == True:
							player.setFours(helper.upperScore(currentHand,4))
							player.removeDecision("fours")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
    					else:
						player.setFours(helper.upperScore(currentHand,4))
						player.removeDecision("fours")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "fives" in decision.lower():
				if "fives" in player.getDecisionList():
					if 5 not in currentHand:
						if giveScoreUp("Fives") == True:
							player.setFives(helper.upperScore(currentHand,5))
							player.removeDecision("fives")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					else:
						player.setFives(helper.upperScore(currentHand,5))
						player.removeDecision("fives")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "sixes" in decision.lower():
				if "sixes" in player.getDecisionList():
		    			if 6 not in currentHand:
						if giveScoreUp("Sixes") == True:
							player.setSixes(helper.upperScore(currentHand,6))
							player.removeDecision("sixes")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					else:
						player.setSixes(helper.upperScore(currentHand,6))
						player.removeDecision("sixes")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "3 of a kind" in decision.lower():
				if "3 of a kind" in player.getDecisionList() and helper.threeOfKind(currentHand):
	    				player.setSetOfThree(helper.chance(currentHand))
					player.removeDecision("3 of a kind")
					valid = 1
				elif "3 of a kind" in player.getDecisionList() and helper.threeOfKind(currentHand) == False:
					if giveScoreUp("Three of a Kind") == True:
						player.removeDecision("3 of a kind")
						valid = 1
				else:
					print("Not a valid selection, please try again.")	
			elif "4 of a kind" in decision.lower():
				if "4 of a kind" in player.getDecisionList() and helper.threeOfKind(currentHand):
	    				player.setSetOfFour(helper.chance(currentHand))
					player.removeDecision("4 of a kind")
					valid = 1
				elif "4 of a kind" in player.getDecisionList() and helper.threeOfKind(currentHand) == False:
					if giveScoreUp("Four of a Kind") == True:
						player.removeDecision("4 of a kind")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "full house" in decision.lower():
    				if "Full House" in player.getDecisionList() and helper.fullHouse(currentHand):
		    			player.setFullHouse()
					player.removeDecision("Full House")
					valid = 1
				elif "Full House" in player.getDecisionList() and helper.fullHouse(currentHand) == False:
					if giveScoreUp("full house") == True:
						player.removeDecision("Full House")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "small straight" in decision.lower():
   				if "Small Straight" in player.getDecisionList() and helper.smallStraight(currentHand) == True:
	    				player.setSmallStraight()
					player.removeDecision("Small Straight")
					valid = 1
   				elif "Small Straight" in player.getDecisionList() and helper.smallStraight(currentHand) == False:
					if giveScoreUp("small straight") == True:
						player.removeDecision("Small Straight")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "large straight" in decision.lower():
				if "Large Straight" in player.getDecisionList() and helper.largeStraight(currentHand):
	    				player.setLargeStraight()
					player.removeDecision("Large Straight")
					valid = 1
				elif "Large Straight" in player.getDecisionList() and helper.largeStraight(currentHand) == False:
					if giveScoreUp("large straight") == True:
						player.removeDecision("Large Straight")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "chance" in decision.lower():
				if "Chance" in player.getDecisionList():
					player.setChance(helper.chance(currentHand))
					player.removeDecision("Chance")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "help" in decision.lower():
				print("Possible moves:" + str(player.getDecisionList()))
			elif "yahtzee" in decision.lower():
				if helper.yahtzee(currentHand) != True:
					if giveScoreUp("Yahtzee") == True:
						player.removeDecision("Yahtzee")
						valid = 1	
				elif player.getnumOfYahtzee() == 0 and helper.yahtzee(currentHand) == True:
					print("YAHTZEE!!")
					player.setYahtzee()
					player.removeDecision("Yahtzee")
					valid = 1
				elif player.getnumOfYahtzee() == 1 and helper.yahtzee(currentHand) == True:
					print("JOKER!! Select another Row to be filled also")
					makeDecision(player, currentHand, helper) #call function again
					player.setYahtzee()
					valid = 1
				else:
					print("Not a valid selection, please try again.")	
			else:
				print("Please enter a valid row")
	

#MAIN DRIVER
	
	print("\nWelcome to YAHTZEE!\n")
	print("-------\t-------\t-------\t-------\t-------\t-------")
	print("|     |\t|o    |\t|o    |\t|o   o|\t|o   o|\t|o   o|")
	print("|  o  |\t|     |\t|  o  |\t|     |\t|  o  |\t|o   o|")
	print("|     |\t|    o|\t|    o|\t|o   o|\t|o   o|\t|o   o|")
	print("-------\t-------\t-------\t-------\t-------\t-------\n")

	playerInput = raw_input('Who is playing the game? (comma separated: e.g. Bob,Jane,Joe)?\n')	
	playerInput = playerInput.split(',')
	players = []	

	for input in playerInput:
		players.append(ScoreCard(str(input)))

	rounds = 13 # number of rounds per game
	dice = Roll()

	for x in range(rounds):
		for player in players:
			printScoreCard(player)
			for y in range(3):
				dice.diceRoll() #roll the dice
				if y == 2:
					break

				decision = raw_input("Reroll or Score?\nDefault is Reroll, if 'score' isn't explicitly stated, you will reroll...\n")
		
				if "score" in decision.lower():
					break
				else:
					dice.diceToKeep() #select which dice to keep
					dice.returnDice() #return some possible dices you don't want anymore
	
			print("\nEnd of turn!\n")
			decisionHand = dice.lastTurn() #get list of current dices
			print("current Hand: " + str(decisionHand) + "\n")
			makeDecision(player, decisionHand, dice)
			print("\nSCORECARD UPDATED:\n*****************")
			printScoreCard(player)
			print("__________________________\n")

	print("end of game")

	winningScore = -1
	winningPlayer = ""

	for player in players:
		print(player.getName() + " total score = " + str(player.totalScore()) + "\n")
		if player.totalScore() > winningScore:
			winningPlayer = player.getName()
			winningScore = player.totalScore()

	print(winningPlayer + " IS THE WINNER! CONGRATS! YOU ARE THE BIG HOT POTATO!\n")
