import os,sys,random,pygame
from pygame.locals import *
import cPickle as pickle

game_options=file('options','wb')
pickle.dump(str(0),game_options)
pickle.dump(str(1024),game_options)
pickle.dump(str(1),game_options)
game_options.close()
