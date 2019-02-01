import pygame

########################################### GLOBAL VALUE ##############################
clock = None
WHITE                = (255, 255, 255)
DisplayWidth         = 470
DisplayHeight        = 640
DisplayObj           = None
ImgBack = pygame.image.load("image/back.png")

########################################## GLOBAL VALUE ##############################



######################################### Function ##################################
def IotSetCaption(caption):
	pygame.display.set_caption(caption)

def IotBackDraw():
	global DisplayObj
	global ImgBack
	DisplayObj.blit(ImgBack, (0,0))

def IotGo():
	global DisplayObj
	global clock

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			pygame.quit()
			break;
		DisplayObj.fill(WHITE)
		IotBackDraw()
		pygame.display.update()
		clock.tick(60)
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
