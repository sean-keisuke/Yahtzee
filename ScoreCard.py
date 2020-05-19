'''
Sean Mullarkey
Yahtzee Player's Scorecard
'''

class ScoreCard:

	def __init__(self):
		self.ones = 0
		self.twos = 0
		self.threes = 0
		self.fours = 0
		self.fives = 0
		self.sixes = 0
		self.setOfThree = 0
		self.setOfFour = 0
		self.fullHouse = 0
		self.smallStraight = 0
		self.largeStraight = 0
		self.chance = 0
		self.yahtzee = 0
		self.numOfYahtzee = 0
	
	def setYahtzee(self):
		if numOfYahtzee == 0:
			self.numOfYahtzee = 1
			self.yahtzee = 50
		else:
			self.yahtzee += 100
		
		return self.numOfYahtzee #flag to notify any further yahtzee is bonus		
			
	def addUpper(self):
		upVal = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes
		if upVal >= 63:
			upVal += 35
		return upVal

	def totalScore(self):
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

	def getSmallStraight(self):
		return self.smallStraight

	def setSmallStraight(self):
		self.smallStraight = 30

	def getLargeStraight(self):
		return self.largeStraight

	def setLargeStraight(self):
		self.largeStraight = 40

	def getChance(self):
		return self.chance

	def setChance(self, n):
		self.chance = n
	
	def getYahtzee(self):
		return yahtzee	
