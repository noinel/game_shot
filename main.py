import pygame

########################################### GLOBAL VALUE ##############################
WHITE                = (255, 255, 255)
DisplayWidth         = 470
DisplayWeight        = 640
DisplayObj           = None

########################################## GLOBAL VALUE ##############################



######################################### Function ##################################
def base:
	global DisplayObj
	pygame.init()
	DisplayObj = pygame.display.set_mode((DisplayWidth, DisplayHeight))
######################################### Function ##################################


