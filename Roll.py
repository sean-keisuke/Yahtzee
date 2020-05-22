'''
Sean Mullarkey
Yahtzee Dice Rolls
'''
import random

class Roll:

	def __init__(self):
		self.currentDiceList = [6,6,6,6,6] 
	    	self.currentKeep = []
		self.currentRoll = 3

	def resetCurrRoll(self):
		self.currentRoll+=1

	def getCurrentDice(self):
		return self.currentDiceList

	def getKeep(self):
		return self.currentKeep

	def diceRoll(self): #Rolls for each turn
		if self.currentRoll == 3: #first turn
	        	self.currentKeep *= 0 
        		self.currentDiceList = [random.randint(1,6) for die in range(0,5)] 
			self.currentRoll = self.currentRoll - 1 #Decrement num of times we rolled so far			
			print 'Current Roll: ' + str(self.currentDiceList)[1:-1] + '\tCurrent Hand: ' + str(self.currentKeep)[1:-1] + '\nRolls left: ' + str(self.currentRoll)
        	else: # 2/3 turn
        		self.currentDiceList = [random.randint(1,6) for die in range(0,5 - (len(self.currentKeep)))] 
			self.currentRoll = self.currentRoll - 1 #Decrement num of times we rolled so far			
			print 'Current Roll: ' + str(self.currentDiceList)[1:-1] + '\tRolls left: ' + str(self.currentRoll) 
			if self.currentRoll == 0: # end of turn
				#print 'end of turn'
				self.lastTurn() #keep the remaining dice 
		return self.currentDiceList 

	def diceToKeep(self): #user input decides which dices to keep after roll
		valid = 0
		while valid != 1:
			keepInput = raw_input('which dice do you want to keep (comma separated: e.g. 1,1,5)?\nIf you do not want to keep any just leave entry blank\nCurrent Rolls: ' + str(self.currentDiceList)[1:-1] + '\n')
			print("Current Rolls: " + str(self.currentDiceList)[1:-1] + "\n")
			if keepInput.isspace() or not keepInput:
				return self.currentDiceList #user doesn't want to keep any die
			else:
				keepInput = keepInput.split(',')

				dices = [item for item in keepInput]
				for die in dices:
					if die.isdigit() == False:
						print("\n" + str(die) + " is not a valid dice, try again!\n")
						valid = 0
						break
					elif int(die) in self.currentDiceList:
						self.currentKeep.append(int(die))
						self.currentDiceList.remove(int(die))
						valid = 1
					else:
						print("\n" + str(die) + " is not an available dice")
						print("\nCurrent Hand: " +str(self.currentKeep)) 
						print("\nCurrent Roll: " +str(self.currentDiceList)) 
						valid = 0
						break
		return self.currentDiceList

	def returnDice(self):
		valid = 0
		while valid != 1:
			returnInput = raw_input('which dice do you want to return (comma separated: e.g. 1,1,5)?\nIf you do not want to return any just leave it blank\nCurrent Hand: ' + str(self.currentKeep)[1:-1] + '\n')
			if returnInput.isspace() or not returnInput:
				return self.currentDiceList #user doesn't want to keep any die
			else:
				returnInput = returnInput.split(',')
				dices = [item for item in returnInput]
				for die in dices:
					if die.isdigit() == False:
						print("\n" + str(die) + " is not a valid dice, try again!\n")
						valid = 0
						break
					elif int(die) in self.currentKeep:
						self.currentDiceList.append(int(die))
						self.currentKeep.remove(int(die))
						valid = 1
					else:
						print("\n" + str(die) + " is not an available dice")
						print("\nCurrent Hand: " +str(self.currentKeep)) 
						print("\nCurrent Roll: " +str(self.currentDiceList)) 
						valid = 0
						break
		return self.currentDiceList		

	def lastTurn(self): #forced to keep everything before new round
		finalHand = self.currentDiceList + self.currentKeep

		self.currentRoll = 3	# reset roll counter
		return finalHand		

	def upperScore(self,dice_list,check_value): #upper column (1's 2's etc)
    		roll_score = 0
        	for die in dice_list:
        		if die == check_value: 
        	   		roll_score += die
    		return roll_score 

	# functions for special Rolls or lower region of scorecard

	def yahtzee(self, dice_list):    
		if len(set(dice_list)) == 1: #no duplicates
        		return True
		return False

	def fullHouse(self, dice_list): #a set of 2 and set of 3
		dice_list.sort()
		if len(set(dice_list)) == 2 and (dice_list[0] != dice_list[3] or dice_list[1] != dice_list[4]):
			return True
		return False

	def largeStraight(self, dice_list): #2,3,4,5,6 or 1,2,3,4,5
		dice_list.sort()
		if len(set(dice_list)) < 5:
			return False
		elif dice_list[4] - dice_list[0] == 4:
			return True
		return False

	def smallStraight(self, dice_list): #1,1,2,3,4 etc
		dice_list.sort()
		if len(set(dice_list)) < 4:
			return False
		elif dice_list[4] - dice_list[0] == 3: # 1,1,2,3,4 or 1,2,3,4,4 etc
			return True
		elif dice_list[3] - dice_list[0] == 3: # 1,2,3,4,6
			return True
		elif dice_list[4] - dice_list[1] == 3: # 1,3,4,5,6
			return True
		return False

	def fourOfKind(self, dice_list): #ex 1,1,1,1,4 or 5,1,1,1,1 etc
		dice_list.sort()
		if len(set(dice_list)) > 2:
			return False
		elif dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
			return True
		return False

	def threeOfKind(self, dice_list): #xxxyz or yxxxz or yzxxx
		dice_list.sort()
		if len(set(dice_list)) > 3:
			return False
		elif dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
			return True
		return False

	def chance(self, dice_list): #add everything
		roll_score = 0
		for die in dice_list:
			roll_score += die
		return roll_score



