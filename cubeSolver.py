clockwise = [6, 3, 0, 7, 4, 1, 8, 5, 2]
counterClockwise = [2, 5, 8, 1, 4, 7, 0, 3, 6]

class Cube:
	def __init__(self):
		'''self.front = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
		self.top = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
		self.bottom = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
		self.left = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
		self.right = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
		self.back = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']'''
		self.front = ['B', 'G', 'G', 'O', 'R', 'B', 'R', 'W', 'O']
		self.top = ['Y', 'G', 'R', 'B', 'Y', 'Y', 'Y', 'W', 'R']
		self.bottom = ['W', 'R', 'W', 'W', 'W', 'Y', 'W', 'B', 'Y']
		self.left = ['O', 'W', 'O', 'G', 'B', 'G', 'O', 'O', 'B']
		self.right = ['Y', 'R', 'W', 'Y', 'G', 'R', 'B', 'O', 'R']
		self.back = ['G', 'R', 'G', 'B', 'O', 'Y', 'B', 'O', 'G']
	def printCube(self):
		print("        "+self.left[0]+"|"+self.left[1]+"|"+self.left[2])
		print("        "+self.left[3]+"|"+self.left[4]+"|"+self.left[5])
		print("        "+self.left[6]+"|"+self.left[7]+"|"+self.left[8])
		print("")
		print(" "+self.back[2]+"|"+self.back[5]+"|"+self.back[8]+"  "+self.bottom[6]+"|"+self.bottom[3]+"|"+self.bottom[0]+"  "+self.front[6]+"|"+self.front[3]+"|"+self.front[0]+"  "+self.top[6]+"|"+self.top[3]+"|"+self.top[0])
		print(" "+self.back[1]+"|"+self.back[4]+"|"+self.back[7]+"  "+self.bottom[7]+"|"+self.bottom[4]+"|"+self.bottom[1]+"  "+self.front[7]+"|"+self.front[4]+"|"+self.front[1]+"  "+self.top[7]+"|"+self.top[4]+"|"+self.top[1])
		print(" "+self.back[0]+"|"+self.back[3]+"|"+self.back[6]+"  "+self.bottom[8]+"|"+self.bottom[5]+"|"+self.bottom[2]+"  "+self.front[8]+"|"+self.front[5]+"|"+self.front[2]+"  "+self.top[8]+"|"+self.top[5]+"|"+self.top[2])
		print("")
		print("        "+self.right[8]+"|"+self.right[7]+"|"+self.right[6])
		print("        "+self.right[5]+"|"+self.right[4]+"|"+self.right[3])
		print("        "+self.right[2]+"|"+self.right[1]+"|"+self.right[0])
		'''
		    LLL               012
		    LLL               345
		    LLL               678
		BBB OOO FFF TTT   258 630 630 630
		BBB OOO FFF TTT   147 741 741 741
		BBB OOO FFF TTT   036 852 852 852
		    RRR               876
		    RRR               543
		    RRR 		      210
		'''
	def frontTurn(self):
		tempFront = self.front[:]
		tempTop = self.top[:]
		tempLeft = self.left[:]
		tempBottom = self.bottom[:]
		tempRight = self.right[:]
		
		self.top[6] = tempLeft[8]
		self.right[0] = tempTop[6]
		self.bottom[2] = tempRight[0]
		self.left[8] = tempBottom[2]
		
		self.top[7] = tempLeft[5]
		self.right[3] = tempTop[7]
		self.bottom[1] = tempRight[3]
		self.left[5] = tempBottom[1]
		
		self.top[8] = tempLeft[2]
		self.right[6] = tempTop[8]
		self.bottom[0] = tempRight[6]
		self.left[2] = tempBottom[0]			
			
		for x in range(0,9):
			self.front[x] = tempFront[clockwise[x]]
	def frontTurnPrime(self):
		tempFront = self.front[:]
		tempTop = self.top[:]
		tempLeft = self.left[:]
		tempBottom = self.bottom[:]
		tempRight = self.right[:]
		
		self.top[6] = tempRight[0]
		self.right[0] = tempBottom[2]
		self.bottom[2] = tempLeft[8]
		self.left[8] = tempTop[6]
		
		self.top[7] = tempRight[3]
		self.right[3] = tempBottom[1]
		self.bottom[1] = tempLeft[5]
		self.left[5] = tempTop[7]
		
		self.top[8] = tempRight[6]
		self.right[6] = tempBottom[0]
		self.bottom[0] = tempLeft[2]
		self.left[2] = tempTop[8]					
			
		for x in range(0,9):
			self.front[x] = tempFront[counterClockwise[x]]	
	'''def leftTurn(self):
	def leftTurnPrime(self):
	def rightTurn(self):
	def rightTurnPrime(self):'''
	def backTurn(self):
	def backTurnPrime(self):
	def topTurn(self):
		tempTop = self.top[:]
		tempFront = self.front[:]
		tempLeft = self.left[:]
		tempBack = self.back[:]
		tempRight = self.right[:]
		
		for x in range(0,3):
			self.front[x] = tempRight[x]
			self.left[x] = tempFront[x]
			self.back[x] = tempLeft[x]
			self.right[x] = tempBack[x]
			
		for x in range(0,9):
			self.top[x] = tempTop[clockwise[x]]		
	def topTurnPrime(self):
		tempTop = self.top[:]
		tempFront = self.front[:]
		tempLeft = self.left[:]
		tempBack = self.back[:]
		tempRight = self.right[:]
		
		for x in range(0,3):
			self.front[x] = tempLeft[x]
			self.left[x] = tempBack[x]
			self.back[x] = tempRight[x]
			self.right[x] = tempFront[x]
			
		for x in range(0,9):
			self.top[x] = tempTop[counterClockwise[x]]
	def bottomTurn(self):
		tempBottom = self.bottom[:]
		tempFront = self.front[:]
		tempLeft = self.left[:]
		tempBack = self.back[:]
		tempRight = self.right[:]
		
		for x in range(6,9):
			self.front[x] = tempLeft[x]
			self.left[x] = tempBack[x]
			self.back[x] = tempRight[x]
			self.right[x] = tempFront[x]
			
		for x in range(0,9):
			self.bottom[x] = tempBottom[clockwise[x]]
	def bottomTurnPrime(self):
		tempBottom = self.bottom[:]
		tempFront = self.front[:]
		tempLeft = self.left[:]
		tempBack = self.back[:]
		tempRight = self.right[:]
		
		for x in range(6,9):
			self.front[x] = tempRight[x]
			self.left[x] = tempFront[x]
			self.back[x] = tempLeft[x]
			self.right[x] = tempBack[x]
			
		for x in range(0,9):
			self.bottom[x] = tempBottom[counterClockwise[x]]
	
		
cube = Cube()
cube.printCube()
cube.bottomTurnPrime()
print("")
cube.printCube()