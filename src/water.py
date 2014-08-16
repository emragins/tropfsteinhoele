import ika
import game 
import frog
import stalactite
import engine
import collision

class Water:

	def __init__(self, x, y, vol, size):
	
		self.x = x
		self.y = y
		self.w = size	#for collission detection
		self.h = size
		self.vol = vol
		
		self.used = False
		self.linger_end = 0
		self.dead = False
		
	def Update(self):
		if self.used == False:
			for a in engine.rungame.frogs:
				if self.used == True:
					pass
				elif collision.DetectCollision(a, self):
					a.increaseWater(self.vol)
					self.used = True
			self.used = True
			self.linger_end = ika.GetTime()+200
		if self.linger_end < ika.GetTime():
			self.dead = True
		
	def Render(self):
		ika.Video.DrawRect(self.x+2,self.y+2,self.x+self.w-2, self.y+self.h-2, ika.RGB(0,0,150), 1, 3)