from scenes import *

class Mapping(object):

#all the scenes in a dictionary for order
    scenes = {
        'intro': Intro(), 'bunker': Bunker(), 'hull': Hull(), 'the_bridge': TheBridge(), 'pod': Pod(), 'escape_ship': EscapeShip(), 
        'mysterious_planet': MysteriousPlanet()
    }

#makes current scene start scene 
    def __init__(self, start_scene):
        self.start_scene = start_scene

#gets the next scene and 
    def next_scene(self, scene_name):
        val = Mapping.scenes.get(scene_name)
        return val

#starts the game with an opening scene
    def opening_scene(self):
        return self.next_scene(self.start_scene)