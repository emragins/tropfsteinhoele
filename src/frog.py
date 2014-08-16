import ika
import engine
import game
import collision
import manager

class Frog:
	
	frogimg = ika.Image("gfx\\frog.png")
	
	max_waterlvl = 100
	
	def __init__(self, x, y, special):
		
		self.x = x
		self.y = y
		self.w = engine.TILE_SIZE	#for collission detection
		self.h = engine.TILE_SIZE
		
		self.alive = True
		self.dead = False	#for rendering
		self.pregnant = 0
		self.birth_time = 0
		
		self.special = special
		
		self.sex = ika.Random(0,2)	#male: 0;   female: 1
			
		self.waterlvl = self.max_waterlvl	#   (-1) will be used for grey frogs--might be a mistake for future updates
		
		self.movenum = ika.Random(0,9)  #direction from top left clockwise, 0 is center
		
		
	def Render(self):
		a = int(self.x)
		b = int(self.y)
		if self.alive == False:
			ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(0,0,0))	#frog dead
		elif self.special == True:
			ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(100,100,100,255))  #grey
		elif self.pregnant == False:
			if self.waterlvl > 66:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(0,255,0,255)) #frog bright green
			elif self.waterlvl > 33:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(120,170,0,255))	#frog pale green
			elif self.waterlvl > 1:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(50,80,0, 255)) 	#frog brown			
		else:
			if self.waterlvl > 66:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(255,0,0, 255)) #frog bright green
			elif self.waterlvl > 33:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(170,0,0, 255))	#frog pale green
			elif self.waterlvl > 1:
				ika.Video.TintBlit(self.frogimg, a,b, ika.RGB(100,0,0, 255)) 	#frog brown
				
	def Update(self):
		if self.special == False:
			if self.waterlvl > 0:
				self.move()
				self.decreaseWater(1)	
			if self.pregnant == False:
				for a in engine.rungame.frogs:
					if collision.DetectCollision(a, self):
						if a.pregnant == False:
							if self.sex == 1 and a.sex == 0:
								self.becomepregnant() 
							elif self.sex == 0 and a.sex == 1:
								a.becomepregnant()
			if self.pregnant == True:
				if ika.GetTime() > self.birth_time:
					engine.rungame.entities.append(Frog(self.x, self.y, True))
					self.pregnant = False
		else:
			self.move()
				
	
	def move(self):
		if ika.Random(1,5) == 4:
			self.movenum = ika.Random(0,9)
						
		if self.movenum == 1:
			self.x -= engine.TILE_SIZE
			self.y -= engine.TILE_SIZE
		elif self.movenum == 2:
			self.y -= engine.TILE_SIZE
		elif self.movenum == 3:
			self.x += engine.TILE_SIZE
			self.y -= engine.TILE_SIZE
		elif self.movenum == 4:
			self.x += engine.TILE_SIZE
		elif self.movenum == 5:
			self.x += engine.TILE_SIZE
			self.y += engine.TILE_SIZE
		elif self.movenum == 6:
			self.y += engine.TILE_SIZE
		elif self.movenum == 7:
			self.x -= engine.TILE_SIZE
			self.y += engine.TILE_SIZE
		elif self.movenum == 8:
			self.x -= engine.TILE_SIZE
		else: 
			pass	#frog does not move
			
		#keep frog on screen
		if self.x < 0:
			self.x = 0
		elif self.x >= engine.WIN_WIDTH:
			self.x = engine.WIN_WIDTH - engine.TILE_SIZE
		if self.y < 0:
			self.y = 0
		elif self.y >= engine.WIN_HEIGHT:
			self.y = engine.WIN_HEIGHT - engine.TILE_SIZE
			
		
	def decreaseWater(self, dif):
		self.waterlvl -= dif
		if self.waterlvl <= 0:
			self.waterlvl = 0
			self.dies()
			
	def dies(self):
		self.alive = False
		self.pregnant = False
		self.w = 0		#remove collusion possibility
		self.h = 0
		
	def increaseWater(self, dif):
		print "increase frog water"
		self.waterlvl += dif
		if self.waterlvl > self.max_waterlvl:
			self.waterlvl = self.max_waterlvl
				
	def becomepregnant(self):
		self.pregnant = True
		self.birth_time = ika.GetTime()+1000  #must live for num/100 seconds
	