import ika
import frog
import engine
import water

class Stalactite:
	
	stalacimg = ika.Image("gfx\\stalactite.png")
	
	def __init__(self, x, y, name):
		
		
		
		self.x = x
		self.y = y
		
		self.name = name
		self.water = 0
		self.max_water = 32
		self.notladen = True
		self.dead = False
		
	def Render(self):
		ika.Video.Blit(self.stalacimg, self.x, self.y) #stalac
		ika.Video.DrawRect(self.x-20, self.y, self.x-10, self.y+self.water, ika.RGB(50,70,150), 1, 2) #water
		engine.font.Print(self.x+ 35, self.y + 10, self.name) #print name, too
		
	def Update(self):
		self.increasewater(1)
		if ika.Input.keyboard[self.name].Pressed():
			if self.water >= 0.5*self.max_water:
				self.dropwater()
		
	def increasewater(self, dif):
		self.water += dif
		if self.water > 32:
			self.water = 32
			if self.notladen == True:
				self.next_update = ika.GetTime()+250
				self.notladen = False
			if ika.GetTime() > self.next_update:
				self.dropwater()
				self.notladen = True
		
	def dropwater(self):
		#if self.notladen == False:
		engine.rungame.entities.append(water.Water(self.x-engine.TILE_SIZE, self.y, \
			self.water, 3*engine.TILE_SIZE)) 	#make water splash
		'''
		else:
			engine.rungame.entities.append(water.Water(self.x, self.y+engine.TILE_SIZE, \
				self.water, engine.TILE_SIZE))
		'''
		self.water = 0
		#give water to frog below