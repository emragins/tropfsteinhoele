import ika
import frog
import engine
import manager
import stalactite
import text

class game:
	entities = []
	frogs = []
	brownbg = ika.Image("gfx\\brownbg.png")
	
	def __init__(self):
		manager.render.append(self.Render)
		manager.update.append(self.Update)
	
	def Update(self):
		pos = 0
		specialfrogs = 0
		for x in self.entities:
			x.Update()
			if x.dead == True:
				del self.entities[pos]
			pos += 1
			
			if hasattr(x, 'special') and x.special == True:
				specialfrogs += 1
		
		if specialfrogs >= 2:
			text.text(10,10, ["Well done, stalactites.  Frogs now inhabit the", 
				"bottom of our cavern."])
			ika.Exit()
			
		frogsalive = False
		for x in self.frogs:
			x.Update()
			if x.alive == True:
				frogsalive = True
		if frogsalive == False:
			text.text(10,10, ["You were unable to keep the frogs moist long enough."])
			self.reset()
			engine.startgame(0)
			
					
	def Render(self):
		ika.Video.Blit(self.brownbg,0,0)
		for x in self.entities:
			if hasattr(x,'Render'):
				x.Render()
		for x in self.frogs:
			x.Render()
	
	def reset(self):
		length = len(self.entities)
		for x in self.entities:
			self.entities.pop(length-1)
			length -= 1
		
		
	
def generatefrogs(numfrogs):
	for x in range(numfrogs):
		x_coord = 32*ika.Random(0,engine.WIN_WIDTH/32)
		y_coord = 32*ika.Random(0,engine.WIN_HEIGHT/32)
		game.frogs.append(frog.Frog(x_coord, y_coord, False))
	
def generatestalactites(numstalac):  #numstalac not presently used
	x_coord = 3*engine.TILE_SIZE
	y_coord = engine.TILE_SIZE*2
	game.entities.append(stalactite.Stalactite(x_coord,y_coord, 'Q'))
	
	x_coord = 14*engine.TILE_SIZE
	y_coord = engine.TILE_SIZE*2
	game.entities.append(stalactite.Stalactite(x_coord,y_coord, 'E'))
	
	x_coord = engine.TILE_SIZE*9
	y_coord = engine.TILE_SIZE*6
	game.entities.append(stalactite.Stalactite(x_coord,y_coord, 'W'))
	
	x_coord = engine.TILE_SIZE*3
	y_coord = engine.TILE_SIZE*10
	game.entities.append(stalactite.Stalactite(x_coord,y_coord, 'A'))
	
	x_coord = engine.TILE_SIZE*14
	y_coord = engine.TILE_SIZE*10
	game.entities.append(stalactite.Stalactite(x_coord,y_coord, 'D'))
	