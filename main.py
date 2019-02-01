import pygame

########################################### GLOBAL VALUE ##############################
clock = None
WHITE                = (255, 255, 255)
DisplayWidth         = 470
DisplayHeight        = 840
DisplayObj           = None
ImgBackA             = pygame.image.load("image/back.png")
ImgBackB             = ImgBackA.copy()
########################################## GLOBAL VALUE ##############################



######################################### Function ##################################
def IotSetCaption(caption):
	pygame.display.set_caption(caption)

def IotBackDraw(Image,x,y):
	global DisplayObj
	global ImgBack
	DisplayObj.blit(Image, (x,y))

def IotGo():
	global DisplayObj
	global clock

	BackAPosY = 0
	BackBPosY = -DisplayHeight

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			pygame.quit()
			break;

		DisplayObj.fill(WHITE)

		BackAPosY = BackAPosY + 2 
		BackBPosY = BackBPosY + 2 
		if DisplayHeight <= BackAPosY:
			BackAPosY = 0
			BackBPosY = -DisplayHeight

		IotBackDraw(ImgBackA,0,BackAPosY)
		IotBackDraw(ImgBackB,0,BackBPosY)

		pygame.display.update()
		clock.tick(10)
	pygame.quit()

def Base():
	global DisplayObj
	global clock

	pygame.init()
	IotSetCaption("IOT GAME")
	DisplayObj = pygame.display.set_mode((DisplayWidth, DisplayHeight))
	clock = pygame.time.Clock()
	IotGo()
######################################### Function ##################################

Base()
