#from sys import exit
#from random import randint
#from textwrap import dedent
#starts the game
import engine, mapping

map = mapping.Mapping('intro')
game = engine.Engine(map)
game.play()

