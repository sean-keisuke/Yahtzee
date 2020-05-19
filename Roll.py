'''
Sean Mullarkey
Yahtzee Dice Rolls
'''
import random

class Roll:


	def __init__(self):
		self._current_dice_list = [6,6,6,6,6] 
        	self._current_kept_dice = [] 
		self._current_Roll = 3

	def roll_dice(self): 
		if self._current_Roll == 3:
        		self._current_kept_dice *= 0 
        		self._current_dice_list = [random.randint(1,6) for die in range(0,5)] 
			self._current_Roll = self._current_Roll - 1 #increment num of times we rolled so far			
			print 'Current Roll: ' + str(self._current_dice_list)[1:-1] + '\tRolls left: ' + str(self._current_Roll) 		 		
        	else:
        		self._current_dice_list = [random.randint(1,6) for die in range(0,5 - (len(self._current_kept_dice)))] 
			self._current_Roll = self._current_Roll - 1 #increment num of times we rolled so far			
			print 'Current Roll: ' + str(self._current_dice_list)[1:-1] + '\tRolls left: ' + str(self._current_Roll) 
			if self._current_Roll == 0: # end of turn
				print 'end of turn'
				self._current_Roll = 3				 
		
		return self._current_dice_list 

	def single_values(self,dice_list,check_value):
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

	def Straight(self, dice_list): #2,3,4,5,6 or 1,2,3,4,5
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



