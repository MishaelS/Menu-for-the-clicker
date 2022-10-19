from config import FONT_GAME, SIZE_FONT
from config import WIDTH, HEIGHT, FPS
from config import WHITE, GRAY, GOLDEN
from elements import Elements
from font import Font
import pygame, sys

# ----------------------------------------------------------------------------------------

class Menus:
	def __init__(self, surface, clock):
		pygame.init()
		self.menu = True
		self.selected = 'start'
        
		self.clock = clock
		self.surface = surface

		self.title = Font(self.surface, FONT_GAME, SIZE_FONT+8)
		self.start = Font(self.surface, FONT_GAME, SIZE_FONT+6)
		self.quit  = Font(self.surface, FONT_GAME, SIZE_FONT+6)
		
		
	def start_menu(self):
		while self.menu:
			self.surface.fill((25, 25, 25))
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.menu = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN and self.selected == 'quit':
						self.selected = 'start'
					elif event.key == pygame.K_DOWN and self.selected == 'start':
						self.selected = 'setting'
					elif event.key == pygame.K_DOWN and self.selected == 'setting':
						self.selected = 'quit'
					
					elif event.key == pygame.K_UP and self.selected == 'setting':
						self.selected = 'start'
					elif event.key == pygame.K_UP and self.selected == 'quit':
						self.selected = 'setting'
					elif event.key == pygame.K_UP and self.selected == 'start':
						self.selected = 'quit'
						
					if event.key == pygame.K_RETURN:
						if self.selected == 'start':
							print('start')
							self.start_game()
						elif self.selected == 'setting':
							print('setting')
							self.start_setting()
						elif self.selected == 'quit':
							print('quit')
							self.menu = False
							

			self.title.render('Sourcecodester', color=GOLDEN, pos=(WIDTH/2, HEIGHT/3))
			
			
			if self.selected == 'start':
				self.start.render('START', color=WHITE, pos=(WIDTH/2, HEIGHT/2))
			else:
				self.start.render('START', color=GRAY, pos=(WIDTH/2, HEIGHT/2))
			
			if self.selected == 'setting':
				self.start.render('SETTING', color=WHITE, pos=(WIDTH/2, HEIGHT/1.8))
			else:
				self.start.render('SETTING', color=GRAY, pos=(WIDTH/2, HEIGHT/1.8))
			
			if self.selected == 'quit':
				self.quit.render('QUIT', color=WHITE, pos=(WIDTH/2, HEIGHT/1.6))
			else:
				self.quit.render('QUIT', color=GRAY, pos=(WIDTH/2, HEIGHT/1.6))


			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			pygame.quit()
			sys.exit()
			
		return 0
	
	def start_game(self):
		rectangle = Elements(self.surface, (WIDTH/2, HEIGHT/2), (64, 64), (122, 255, 122))
		game_over = False
		while not game_over:
			self.surface.fill((25, 25, 25))
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						game_over = True


			rectangle.move()
			rectangle.update()
			
			
			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			game_over = False
			
		return 0
	
	def start_setting(self):
		title_setting  = Font(self.surface, FONT_GAME, SIZE_FONT+8)
		back = False
		while not back:
			self.surface.fill((25, 25, 25))
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						back = True
		
		
			title_setting.render('>SETTING<', color=WHITE, pos=(WIDTH/2, HEIGHT/6))
			
			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			back = False
			
		return 0
