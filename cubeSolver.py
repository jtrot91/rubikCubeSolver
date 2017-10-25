
class Cube:
	def __init__(self):
		self.front = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
		self.top = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
		self.bottom = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
		self.left = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
		self.right = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
		self.back = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
	
	def printCube(self):
		print("       "+self.left[0]+"|"+self.left[1]+"|"+self.left[2])
		print("       "+self.left[3]+"|"+self.left[4]+"|"+self.left[5])
		print("       "+self.left[6]+"|"+self.left[7]+"|"+self.left[8])
		print(" "+self.back[2]+"|"+self.back[5]+"|"+self.back[8]+"|"+self.bottom[6]+"|"+self.bottom[3]+"|"+self.bottom[0]+"|"+self.front[6]+"|"+self.front[3]+"|"+self.front[0]+"|"+self.top[6]+"|"+self.top[3]+"|"+self.top[0])
		print(" "+self.back[1]+"|"+self.back[4]+"|"+self.back[7]+"|"+self.bottom[7]+"|"+self.bottom[4]+"|"+self.bottom[1]+"|"+self.front[7]+"|"+self.front[4]+"|"+self.front[1]+"|"+self.top[7]+"|"+self.top[4]+"|"+self.top[1])
		print(" "+self.back[0]+"|"+self.back[3]+"|"+self.back[6]+"|"+self.bottom[8]+"|"+self.bottom[5]+"|"+self.bottom[2]+"|"+self.front[8]+"|"+self.front[5]+"|"+self.front[2]+"|"+self.top[8]+"|"+self.top[5]+"|"+self.top[2])
		print("       "+self.right[8]+"|"+self.right[7]+"|"+self.right[6])
		print("       "+self.right[5]+"|"+self.right[4]+"|"+self.right[3])
		print("       "+self.right[2]+"|"+self.right[1]+"|"+self.right[0])
		'''
		   LLL            012
		   LLL            345
		   LLL            678
		BBBOOOFFFTTT   258630630630
		BBBOOOFFFTTT   147741741741
		BBBOOOFFFTTT   036852852852
		   RRR            876
		   RRR            543
		   RRR		      210
		'''
	'''def frontTurn(self):
	def frontTurnPrime(self):
	def leftTurn(self):
	def leftTurnPrime(self):
	def rightTurn(self):
	def rightTurnPrime(self):
	def backTurn(self):
	def backTurnPrime(self):
	def topTurn(self):
	def topTurnPrime(self):
	def bottomTurn(self):
	def bottomTurnPrime(self):'''
	
		
cube = Cube()
cube.printCube()