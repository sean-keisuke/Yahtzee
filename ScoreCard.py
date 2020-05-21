'''
Sean Mullarkey
Yahtzee Player's Scorecard
'''

class ScoreCard:

	def __init__(self, n):
		self.scoreCardName = n #name of player
		self.ones = -1
		self.twos = -1
		self.threes = -1
		self.fours = -1
		self.fives = -1
		self.sixes = -1
		self.setOfThree = -1
		self.setOfFour = -1
		self.fullHouse = -1
		self.smallStraight = -1
		self.largeStraight = -1
		self.chance = -1
		self.yahtzee = -1
		self.numOfYahtzee = -1
		self.upperBonus = False		

	def getName(self):
		return self.scoreCardName 
	
	def setYahtzee(self):
		if numOfYahtzee == 0:
			self.numOfYahtzee = 1
			self.yahtzee = 50
		else:
			self.yahtzee += 100
		
		return self.numOfYahtzee #flag to notify any further yahtzee is bonus
	
	def yahtzeeToZero(self):
		self.yahtzee = 0
			
	def addUpper(self): #upper region of scorecard
		upVal = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes
		if upVal >= 63: #if 63 or more, a bonus!
			upVal += 35
			self.upperBonus = True
		return upVal
	
	def getUpperBonus(self):
		return self.upperBonus

	def totalScore(self): #add total score!
		total = self.addUpper()
		total += self.setOfThree + self.setOfFour + self.fullHouse + self.smallStraight + self.largeStraight + self.chance + self.yahtzee
		return total

	#boring setters/getters

	def getOnes(self):
		return self.ones

	def setOnes(self, n):
		self.ones = n

	def getTwos(self):
		return self.twos

	def setTwos(self, n):
		self.twos = n

	def getThrees(self):
		return self.threes

	def setThrees(self, n):
		self.threes = n

	def getFours(self):
		return self.fours

	def setFours(self, n):
		self.fours = n

	def getFives(self):
		return self.fives

	def setFives(self, n):
		self.fives = n

	def getSixes(self):
		return self.sixes

	def setSixes(self, n):
		self.sixes = n

	def getSetOfThree(self):
		return self.setOfThree

	def setSetOfThree(self, n):
		self.setOfThree = n

	def getSetOfFour(self):
		return self.setOfFour

	def setSetOfFour(self, n):
		self.setOfFour = n

	def getFullHouse(self):
		return self.fullHouse

	def setFullHouse(self):
		self.fullHouse = 25
	
	def fullHouseZero(self):
		self.fullHouse = 0

	def getSmallStraight(self):
		return self.smallStraight

	def setSmallStraight(self):
		self.smallStraight = 30
	
	def SMStoZero(self):
		self.smallStraight = 0

	def getLargeStraight(self):
		return self.largeStraight

	def setLargeStraight(self):
		self.largeStraight = 40
	
	def LGStoZero(self):
		self.largeStraight = 0

	def getChance(self):
		return self.chance

	def setChance(self, n):
		self.chance = n
	
	def getYahtzee(self):
		return self.yahtzee	
