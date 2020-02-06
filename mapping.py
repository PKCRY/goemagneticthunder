from scenes import *

class Mapping(object):

    scenes = {
        'Intro': Intro(), 'Bunker': Bunker(), 'Hull': Hull(), 'TheBridge': TheBridge(), 'Pod': Pod(), 'EscapeShip': EscapeShip(), 
        'MysteriousPlanet': MysteriousPlanet()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Mapping.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)