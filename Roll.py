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

	def diceRoll(self): 
		if self.currentRoll == 3:
        		self.currentKeep *= 0 
        		self.currentDiceList = [random.randint(1,6) for die in range(0,5)] 
			self.currentRoll = self.currentRoll - 1 #Decrement num of times we rolled so far			
			print 'Current Roll: ' + str(self.currentDiceList)[1:-1] + '\tRolls left: ' + str(self.currentRoll)
        	else:
        		self.currentDiceList = [random.randint(1,6) for die in range(0,5 - (len(self.currentKeep)))] 
			self.currentRoll = self.currentRoll - 1 #Decrement num of times we rolled so far			
			print 'Current Roll: ' + str(self.currentDiceList)[1:-1] + '\tRolls left: ' + str(self.currentRoll) 
			if self.currentRoll == 0: # end of turn
				print 'end of turn'
				self.currentRoll = 3				 
		
		return self.currentDiceList 

	def diceToKeep(self):
		keepInput = raw_input('which dice do you want to keep (comma separated: e.g. 1,1,5)? ')
		keepInput = keepInput.split(',')

		if not keepInput:
			return self.currentDiceList #user doesn't want to keep any die

		dices = [int(item) for item in keepInput]
	
		for die in dices:
			self.currentKeep.append(die)
			
		for value in dices:
			if value in self.currentDiceList:
				self.currentDiceList.remove(value)

		return self.currentDiceList

	def upperScore(self,dice_list,check_value):
    		roll_score = 0
        	for die in dice_list:
            		if die == check_value:
                		roll_score +=die
    		return roll_score 

	#functions for special Rolls
	def yahtzee(self, dice_list):    
		if len(set(dice_list)) == 1: #no duplicates
        		return True
		return False

	def fullHouse(self, dice_list): #a set of 2 and set of 3
		dice_list.sort()
		if len(set(dice_list)) == 2 and (dice_list[0] != dice_list[3] or dice_list[1] != dice_list[4]):
			return True
		return False

	def straight(self, dice_list): #2,3,4,5,6 or 1,2,3,4,5
		dice_list.sort()
		if len(set(dice_list)) == 5 and dice_list[0] == 2 and dice_list[4] == 6:
			return True
		elif len(set(dice_list)) == 5 and dice_list[0] == 1 and dice_list[4] == 5:
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



