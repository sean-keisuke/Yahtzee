'''
Sean Mullarkey
Yahtzee Simulation
'''

from Roll import Roll
from ScoreCard import ScoreCard

class Yahtzee:
	
	def printScoreCard(player):

		def showZero(n):
			if n < 0:
				return 0
			else:
				return n

		print("\nScoreCard for " + str(player.getName()) +  ":\n")
		print("Aces:\t\t" + str(showZero(player.getOnes())))
		print("Twos:\t\t" + str(showZero(player.getTwos())))
		print("Threes:\t\t" + str(showZero(player.getThrees())))
		print("Fours:\t\t" + str(showZero(player.getFours())))
		print("Fives:\t\t" + str(showZero(player.getFives())))
		print("Sixes:\t\t" + str(showZero(player.getSixes())))

		if not player.getUpperBonus():
			print("Upper Bonus:\t0")
		else:
			print("Upper Bonus:\t35")

		print("Upper Total:\t" + str(showZero(player.addUpper())))
		print("\n3 of a kind:\t" + str(showZero(player.getSetOfThree())))
		print("4 of a kind:\t" + str(showZero(player.getSetOfFour())))
		print("Full House:\t" + str(showZero(player.getFullHouse())))
		print("Small Straight:\t" + str(showZero(player.getSmallStraight())))
		print("Large Straight:\t" + str(showZero(player.getLargeStraight())))
		print("Chance:\t\t" + str(showZero(player.getChance())))
		print("Yahtzee:\t" + str(showZero(player.getYahtzee())))
		print("\nTotal Score:\t" + str(showZero(player.totalScore())) + "\n")
	


	def makeDecision( player, currentHand, helper):
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
	    			if player.getOnes() == -1:
		    			if 1 not in currentHand:
						if giveScoreUp("Aces") == True:
							player.setOnes(helper.upperScore(currentHand,6))
							player.removeDecision("aces")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					player.setOnes(helper.upperScore(currentHand,1))
					player.removeDecision("aces")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "twos" in decision.lower():
    				if player.getTwos() == -1:
		    			if 2 not in currentHand:
						if giveScoreUp("Twos") == True:
							player.setTwos(helper.upperScore(currentHand,6))
							player.removeDecision("twos")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
    					player.setTwos(helper.upperScore(currentHand,2))
					player.removeDecision("twos")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "threes" in decision.lower():
    	    			if player.getThrees() == -1:
		    			if 3 not in currentHand:
						if giveScoreUp("Threes") == True:
							player.setThrees(helper.upperScore(currentHand,6))
							player.removeDecision("threes")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					player.setThrees(helper.upperScore(currentHand,3))
					player.removeDecision("threes")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "fours" in decision.lower():
				if player.getFours() == -1:
		    			if 4 not in currentHand:
						if giveScoreUp("Fours") == True:
							player.setFours(helper.upperScore(currentHand,6))
							player.removeDecision("fours")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
    					player.setFours(helper.upperScore(currentHand,4))
					player.removeDecision("fours")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "fives" in decision.lower():
    				if player.getFives() == -1:
					if 5 not in currentHand:
						if giveScoreUp("Fives") == True:
							player.setFives(helper.upperScore(currentHand,6))
							player.removeDecision("fives")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					player.setFives(helper.upperScore(currentHand,5))
					player.removeDecision("fives")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "sixes" in decision.lower():
    				if player.getSixes() == -1:
		    			if 6 not in currentHand:
						if giveScoreUp("Sixes") == True:
							player.setSixes(helper.upperScore(currentHand,6))
							player.removeDecision("sixes")
							valid = 1
						else:
							print("Not a valid selection, please try again.")
					player.setSixes(helper.upperScore(currentHand,6))
					player.removeDecision("sixes")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "3 of a kind" in decision.lower():
    				if player.getSetOfThree() == -1 and helper.threeOfKind(currentHand):
	    				player.setSetOfThree(helper.chance(currentHand))
					player.removeDecision("3 of a kind")
					valid = 1
				elif player.getSetOfThree() == -1 and helper.threeOfKind(currentHand) == False:
					if giveScoreUp("Three of a Kind") == True:
						player.setSetOfThree(0)
						player.removeDecision("3 of a kind")
						valid = 1
				else:
					print("Not a valid selection, please try again.")	
			elif "4 of a kind" in decision.lower():
    				if player.getSetOfFour() == -1 and helper.fourOfKind(currentHand):
	    				player.setSetOfFour(helper.chance(currentHand))
					player.removeDecision("4 of a kind")
					valid = 1
				elif player.getSetOfFour() == -1 and helper.fourOfKind(currentHand) == False:
					if giveScoreUp("Four of a Kind") == True:
						player.setSetOfFour(0)
						player.removeDecision("4 of a kind")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "full house" in decision.lower():
    				if player.getFullHouse() == -1 and helper.fullHouse(currentHand):
		    			player.setFullHouse()
					player.removeDecision("Full House")
					valid = 1
				elif player.getFullHouse() == -1 and helper.fullHouse(currentHand) == False:
					if giveScoreUp("full house") == True:
						player.fullHouseZero()
						player.removeDecision("Full House")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "small straight" in decision.lower():
   				if player.getSmallStraight() == -1 and helper.smallStraight(currentHand) == True:
	    				player.setSmallStraight()
					player.removeDecision("Small Straight")
					valid = 1
				elif player.getSmallStraight() == -1 and helper.smallStraight(currentHand) == False:
					if giveScoreUp("small straight") == True:
						player.SMStoZero()
						player.removeDecision("Small Straight")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "large straight" in decision.lower():
   				if player.getLargeStraight() == -1 and helper.largeStraight(currentHand):
	    				player.setLargeStraight()
					player.removeDecision("Large Straight")
					valid = 1
				elif player.getLargeStraight() == -1 and helper.largeStraight(currentHand) == False:
					if giveScoreUp("large straight") == True:
						player.LGStoZero()
						player.removeDecision("Large Straight")
						valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "chance" in decision.lower():
				if player.getChance() == -1:
					player.setChance(helper.chance(currentHand))
					player.removeDecision("Chance")
					valid = 1
				else:
					print("Not a valid selection, please try again.")
			elif "help" in decision.lower():
				print("Possible moves:" + str(player.getDecisionList()))
			elif "yahtzee" in decision.lower():
				if player.getnumOfYahtzee() == 0 and helper.yahtzee(currentHand) == True:
					player.setYahtzee()
					valid = 1
				elif player.getnumOfYahtzee() == 1 and helper.yahtzee(currentHand) == True:
					print("JOKER!! Select another Row to be filled also")
					makeDecision(player, currentHand, helper) #call function again
					player.setYahtzee()
					valid = 1
				elif helper.yahtzee(currentHand) != True:
					if giveScoreUp("Yahtzee") == True:
						player.yahtzeeToZero()
						player.removeDecision("Yahtzee")
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
