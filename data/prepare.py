"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg
from . import tools


SCREEN_SIZE = (800, 600)
ORIGINAL_CAPTION = "Intro scene with movie"


#Initialization
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


#Resource loading (Fonts and music just contain path names).
FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
MUSIC = tools.load_all_music(os.path.join("resources","music"))
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
MOV   = tools.load_all_movies(os.path.join("resources","movies"))