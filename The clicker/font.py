from config import WIDTH, HEIGHT
import pygame

# ----------------------------------------------------------------------------------------

class Font:
	def __init__(self, surface, font, size):
		pygame.font.init()
		self.font = pygame.font.Font(font, size)
		self.surface = surface
		
	def render(self, text='', smoothing=True, color=(0, 0, 0), pos=(WIDTH/2, HEIGHT/2)):
		self.text = self.font.render(text, smoothing, color)
		self.rect = self.text.get_rect(center=pos)
		self.surface.blit(self.text, self.rect)
