#the map and the engine will all be able to look at eachother and move around scenes based
#on what the player chooses. you should be able to go back and forward 

#can engine also be just map? do i need to create another class for it ?
class Engine(object): 
    #references the mapping to see the order
    def __init__(self, scene_map):
        self.scene_map = scene_map 
    
    #waht actually moves the user from scene to scene
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
        #needs to reference what scene it is currently on and what scene it can move to






