import pygame

# ----------------------------------------------------------------------------------------

class Elements(pygame.sprite.Sprite):
	def __init__(self, surface, img, pos, size):
		self.image_old = pygame.image.load(img).convert_alpha()
		self.image_old = pygame.transform.scale(self.image_old, size)
		self.rect_old = self.image_old.get_rect(center=pos)
		
		self.surface = surface
		
	def move(self):
		pass
	
	def update(self):
		self.surface.blit(self.image_old, self.rect_old)
