import os

# CONSTANT ----------------------------------------------------------------------------------------

NAME_TITEL = 'THE CLICKER'

WIDTH = 576
HEIGHT = 576
FPS = 60

SIZE_WIN = [WIDTH, HEIGHT]
SIZE_FONT = 16
SIZE_IMAGE = 256

PATH_FONT = os.path.join('font', 'Quinquefive-K7qep.ttf')

PATH_IMAGE_LIST = [os.path.join('assets', 'COIN_GOLDEN.png'),
				   os.path.join('assets', 'COIN_COPPER.png'),
				   os.path.join('assets', 'COIN_SILVER.png'),]
				   
PATH_BG = os.path.join('assets', 'BG.png')
PATH_SAVEING = os.path.join('saving', 'save.txt')

WHITE = (255, 255, 255)
GRAY = (55, 55, 55)
DARK_GREY = (35, 35, 35)

GOLDEN = (255, 215, 0)
SILVER = (192, 192, 192)
COPPER = (184, 115, 51)
