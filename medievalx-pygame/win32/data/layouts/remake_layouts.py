import os,sys,random,pygame
from pygame.locals import *
import cPickle as pickle

layout=['bbbbbbbbbbbbbbbbbbbbbbbbbbb',
        'bgggggggggggggpgggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bggggggggggeggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggggegggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggeggggggeggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bgggggggggggggggggggggggggb',
        'bbbbbbbbbbbbbbbbbbbbbbbbbbb']

x=file('layout1.layout','wb')
layoutheight=len(layout)

templayout=str(layout)
print templayout
templayout=templayout.strip('[')
templayout=templayout.strip(']')
print "Final Templayout: "+templayout
newlayout=templayout
print "Final Thing: "
print newlayout
pickle.dump(newlayout,x)
