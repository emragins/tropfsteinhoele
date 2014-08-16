import ika
import frog
import game
import stalactite
import text
import manager

last_fps = 0
font = ika.Font("font.fnt")

WIN_WIDTH = 640
WIN_HEIGHT = 480
TILE_SIZE = 32

def mainloop():
	last_update = 0
	last_update2 = 0
	while 1:
		
		if ika.GetTime() > last_update:
			global last_fps
			
			last_update = ika.GetTime()+10
			
			
			""" from hawk's code"""
			if last_fps != ika.GetFrameRate():
				ika.SetCaption( "Tropfsteinhoehle (FPS: "+str(ika.GetFrameRate())+")" )
				last_fps = ika.GetFrameRate()
			
			ika.Input.Update()
			manager.globalupdate()
			ika.ProcessEntities()
			

		if ika.GetTime() > last_update2:
			ika.Render()
			manager.globalrender()

			ika.Video.ShowPage()
		
			last_update2 = ika.GetTime()+1
		
def intro():
	text.text(10,10, ["Greetings stalactites.  Frogs have inhabited the",
		"bottom of our dreary cave, and it is our goal to keep them",
		"alive until they can produce offspring capable of living",
		"here under their own powers.",
		"",
		"Until then, release the water from yourselves onto the frogs so",
		"that their skin does not dry out.",
		"Best of luck to us all.",
		"",
		"",
		"(Press 'Space' to proceed)"])
	
	startgame(0)  #number for possible future additions of difficulty level

rungame = game.game()
numfrogs = 0
	
def startgame(difficulty):
	global rungame
	
	numstalac = 5	#numstalac not presently used
	
	if difficulty == 0:		#current all-encompasing difficulty: ie. random.
		MINFROGS = 3
		MAXFROGS = 7
		numfrogs = ika.Random(MINFROGS, MAXFROGS)
			
		game.generatefrogs(numfrogs)
		game.generatestalactites(numstalac)
