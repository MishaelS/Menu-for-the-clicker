from elements import Elements
from background import BackGround
from font import Font
from config import *
import pygame, sys, json

# ----------------------------------------------------------------------------------------

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption(NAME_TITEL)
		self.screen = pygame.display.set_mode(SIZE_WIN)
		self.clock = pygame.time.Clock()
		
		self.surface = self.screen
		
		self.menu = True
		self.selected = 'start'
		self.data = {'MONEY': 0}
		
		self.load_file_save()
        
		self.title = Font(self.surface, PATH_FONT, SIZE_FONT+8)
		self.start = Font(self.surface, PATH_FONT, SIZE_FONT+6)
		self.quit  = Font(self.surface, PATH_FONT, SIZE_FONT+6)
		
		self.IMAGE = PATH_IMAGE_LIST[0]
		
		self.bg = BackGround(self.surface, PATH_BG, (WIDTH/2, HEIGHT/2), (WIDTH*1.4, HEIGHT*1.4))
	
# ----------------------------------------------------------------------------------------
	
	def save_when_closing(self):
		with open(PATH_SAVEING, 'w') as file:
			json.dump(self.data, file)
			
	def load_file_save(self):
		try:
			with open(PATH_SAVEING) as file:
				self.data = json.load(file)
		except Exception as error:
			print(f'ERROR: error')
		
# ----------------------------------------------------------------------------------------

	def start_menu(self):
		while self.menu:
			self.surface.fill(DARK_GREY)
			self.bg.update()
			
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
					
					if event.key == pygame.K_UP and self.selected == 'setting':
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
							

			self.title.render(NAME_TITEL, color=GOLDEN, pos=(WIDTH/2, HEIGHT/3))
			
			
			if self.selected == 'start':
				self.start.render('START', color=WHITE, pos=(WIDTH/2, HEIGHT/2))
			else:
				self.start.render('START', color=GRAY, pos=(WIDTH/2, HEIGHT/2))
			
			if self.selected == 'setting':
				self.start.render('SETTING', color=WHITE, pos=(WIDTH/2, HEIGHT/1.7))
			else:
				self.start.render('SETTING', color=GRAY, pos=(WIDTH/2, HEIGHT/1.7))
			
			if self.selected == 'quit':
				self.quit.render('QUIT', color=WHITE, pos=(WIDTH/2, HEIGHT/1.5))
			else:
				self.quit.render('QUIT', color=GRAY, pos=(WIDTH/2, HEIGHT/1.5))


			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			self.save_when_closing()
			pygame.quit()
			sys.exit()
			
		return 0
	
# ----------------------------------------------------------------------------------------

	def start_game(self):
		coin = Elements(self.surface, self.IMAGE, (WIDTH/2, HEIGHT/2), (SIZE_IMAGE, SIZE_IMAGE))
		title_money = Font(self.surface, PATH_FONT, SIZE_FONT+6)
		game_over = False
		while not game_over:
			self.surface.fill(DARK_GREY)
			self.bg.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.save_when_closing()
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						game_over = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.data['MONEY'] += 1
				

			coin.move()
			coin.update()
			
			title_money.render('$ {0}'.format(self.data['MONEY']), color=WHITE, pos=(WIDTH/2, HEIGHT/10))
			
			
			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			game_over = False
			
		return 0
	
# ----------------------------------------------------------------------------------------

	def start_setting(self):
		title_setting = Font(self.surface, PATH_FONT, SIZE_FONT+8)
		back = False
		while not back:
			self.surface.fill(DARK_GREY)
			self.bg.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.save_when_closing()
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						back = True
		
		
			title_setting.render('SETTING', color=WHITE, pos=(WIDTH/2, HEIGHT/6))
			
			pygame.display.flip()
			self.clock.tick(FPS)
		else:
			back = False
			
		return 0
		
# ----------------------------------------------------------------------------------------

def main():
	game = Game()
	game.start_menu()
	return 0
	
# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
