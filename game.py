#from sys import exit
#from random import randint
#from textwrap import dedent

import engine, mapping

map = mapping.Mapping('Intro')
game = engine.Engine(map)
game.play()

