from sys import exit
from random import randint
from textwrap import dedent
import inventory 


#overall scene class
class Scene(object):

#makes a list for the options in all Scene
    def __init__(self):
        self.options = []

#if there is something typed this will run
    def choice(self):
        while True:
            action = input("> ")
            
            #tried to implement the inventory system for all inputs
            if action == 'inventory':
                #self.inventory.Inventory = print_inventory
                
                action = self.choice
            
            #returns whatever the user typed to be checked
            if action in self.options:
                return action
            
            else:
                print("Not a valid input")

#not being used yet
    def enter(self):
        print("this isnt really configured yet just trying to figure it out")
        exit(1)

    

#starting scene for the game
class Intro(Scene):
    def enter(self):
        print(dedent("""
        A rare mineral known as Puraxite has been found near the center of the Milky Way Galaxy
        and the center of attention for many big organizations. 
        This mineral would be the first 100 Percent efficient super conducter in the Milky Way.
        However, instead of sharing this resource the two biggest parties in question decided they wanted a monopoly 
        over the technology. The galactic Overseers and the Milky Way Federation have started a war 
        over this mineral. Years this has been going on. With each Corperation at a standstill. They Don't have
        the technology to mine this Puraxite in a way that would keep it in tact. 

        You have this information and you must decide what to do with it.

        --------------------------------------------------------------------------------------------------------------
         """))
        return 'bunker'

class Bunker(Scene):
    def enter(self):
        print(dedent("""
        "Hey get the hell up! you have some explaining to do!" 

        The loud speaker on the ship is loud but you can tell the tenseness in his voice. 
        You grumble awake and remember your surroundings. Looking around you see the many crates of cargo. 
        In fact you are sleeping up against one of these crates. 
        You have a blanket and some sort of sack that you are resting your head on. 
        You are still groggy and hear the intercom again.

        "Get the hell up!"

        Do you decide to <sleep> or <get up> up to the hull and see what the hell this guy is yelling at you for

        -----------------------------------------------------------------------------------------------------------
         """))

         #use the list to add what options you can choose and then checks them with if else statements
         #repeated for all scenes
        self.options = ['get up', 'sleep']

        option = self.choice()

        if option == 'get up':
            print(dedent("""
            You decide to get up from your makeshift cargo bed and navigate up the stairs 
            to the hull and close the airlocked door behind you

            ------------------------------------------------------------------------------------------------
            """))
            return 'hull'
        
        elif option == 'sleep':
            print(dedent(""" 
            You decide to nod off again. Ignoring the loudspeaker and want to catch a few more zzzzz's.

            As you are about to nod off again...

            BOOOOM!!!!

            A large hole is blasted into the Bunker. You try ot get up and run but the airlock system has
            already been comprimised and you are sucked out into the vaccuum of space trying to scream but 
            because of the lack of oxygen you have no air to use and freeze to death in an instant

            -----------------------------------------------------------------------------------------------
            """))

            return 'bunker'

class Hull(Scene):
    def enter(self):
        print(dedent("""
        Running up the stairs to the hull you look out the windows of the ship. 
        It's very large and almost mesmerizing. Almost. Once you notice 
        all of the blaster cannon shots being fired and ships surrounding this 
        large cargo ship your mood changes

        "There you are you greasy bastard!"

        Before you can whip your head around to see who it was...

        BOOOOM!!!

        You fall to the ground from the shaking. The ship has been hit!
        
        " -The Cargo has been comprimised please take emergency procedures to save any cargo thats left- "

        The robotic voice over the PA system is almsot unnerving. It doesn't match the chaos at hand.

        "YOU!"

        After getting back up to your feer you can see who is calling your name. It's the captain of the ship. 
        You can tell by the uniform he has on and the 
        cap that he is wearing with a special holographic signia.

        "Get the hell over here you liar"

        Instantly your mind starts to grow weary. How did he know that I was lying? My story was pretty 
        well told and there were no loop holes. I am just a hitchiker trying to get to 
        get anywhere in the Delta Quadrent. No other motives. No other information. 

        "You aren't who you say you are lad"
        you respond
        "What do you mean" 
        The whole time you are both yelling over the loud blasts hitting the ships and the crew yelling 
        at eachother to make sure the ship kept running

        "You are a wanted man"

        Shit they figured it out.
        You try to evade the question 
        "I don't think I got your name. Who are you?"

        "I'm Captain Laxian and you need to explain to me why the hell you are wanted otherwise we all die"
        Well the stakes are certianly high.
        "How do you know im a wanted man?"

        Laxian yelled "They jammed our comms and sent a message saying if we don't give up a hitch hiker 
        aboard this ship there would be consequences! I tried to cover your ass like a fool and now I don't 
        think we are going to get out of here alive if you continue to stay on board!"

        Well yeah now they know who I am. Shit. But how the hell did they know I was here. 
        I left the research facility without a trace. All I had on me was the classified data in the 
        memory of my cybernetic implant. There is no way they could track me. 
        
        You yell "Alright well if it is that important I'm a wanted man by both the Galactic Overseers 
        and the Milky Way Federation for information that could change the tide of the war!

        Another blast fills the silence as Laxian stares at you in disbeleif. 

        "What the hell were you thinking getting on my ship!"

        Laxian goes to tackle you to the ground and you struggle to try to get him off of you but to no prevail

        "Why shouldn't I turn you in right now you bastard!"

        Struggling to say the words you respond 
        
        "They just want me right? Is there any way you 
        can eject me out of this ship to a planet near by. I'll get out of your hair and your 
        ship will survive" 

        The Captain releases his grip off of you slowly and ponders your proposal. 

        "The only way we could get you off of this ship is if you take one of the pods with 
        some cargo to hide your escape. But we have to move fast otherwise we will both be dead"

        Laxian gets off of you and you catch your breath and ask 

        "What do we need to do?"


        ---------------------------------------------------------------------------------------------

        """))
        return 'the_bridge'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        Laxian grabs you by the arm in haste and pulls you towards the main bridge of the ship 
        and tells you to look to the side of the ship through the window.
        Blasts are still going around and the main ship seems to be taking considerable damage.

        "The shields won't last much longer." Laxian says in a grim tone
        "I see that Captian. Get me out of here as fast as possible and you should be fine."

        Suddenly Sirens are going off within the ship and red lights are flashing. 
        The robotic voice from before comes over calmly on the loud speaker.

        " -There has been a breach please check breach site- "
        The main holographic screen points to a red dot on the bidge

        Laxian pulls out his gun from his holster quick as Bolard Fox.

        "We need to move fast lad. Or we aren't going to make it." 

        He directs you to follow him closely but to keep an eye out for intruders. The whole crew seems to 
        be up in arms while still trying to maintain the ships vitals
        ypu follow the captian closely to where the bridge was breached

        Both you and the captain are being careful around corners approaching the breach and all of a sudden

        PSSSSSSWWWWEEE

        A blast comes out of the corridor and the Laxian fires back

        PSSSSSSWWWWEEE
        PSSSSSSWWWWEEE
        PSSSSSSWWWWEEE

        Guns are going off all around you do you <take cover> or do you <run> at the bastards
        
        ----------------------------------------------------------------------------------------
        """))

        self.options = ['run', 'take cover']
        option = self.choice()
        

        if option == 'run':
            print(dedent("""
            You run out into the corridor like an idiot and tackle the first guy you see 
            knocking him to the ground. You wrestle him for a bit and punch 
            him in the face to discorient him and get immedietly shot in the head. 
            Not even having a moment to think about the horrible descison you just made.

            
            ----------------------------------------------------------------------------------------------------------
            """))
            return 'the_bridge'

        elif option == 'take cover':
            print(dedent("""
            You take cover behind one of the walls while Laxian fires at the enemy. You hear one AARRGGHH and a body 
            hit the floor and Laxion motions for you to move forward with him. 
            "I'm an idiot I should have given you a  weapon of some sort. Here take this"

            YOU OBTAINED THE GUN 

            You grab the gun and take a quick look. It is sleek and has a light emmitting down the barrel 

            |-----------------------------------------|
            |         |_______________________________|
            |         --------------------------------|
            |         |------------------------------/
            |         |
            |         |
            |         |
            ------------

            Standard Overseer weaponory. You are fairly familiar with it.

            "Alright lad we need to keep moving. The pods are down this way.


            -------------------------------------------------------------------------------------------------------------------
            """))
            
            #self.current_inventory = inventory.Inventory()
            #self.current_inventory.add_item('Gun')

            return 'pod'


class Pod(Scene):
    def enter(self):
        print(dedent("""
        You see a recon enemy ship attached to the side of the frieghter. Other crew members have come to you and the captains 
        aid to clear the rest of the ship out. You here more blasts and more bodies his the ground.
        Then you here the "ALL CLEAR" from the crew on the inside. The pod has been locked down which is good for the ship. 
        "The ship is this way lad. You make sure to check your corners and checking a corner you see a member the overseer crew

        Do you <shoot> at the man or hide back and <alert> the captain?

        ---------------------------------------------------------------------------------------------------------------------------
        """))

        self.options = ['shoot', 'alert']
        option = self.choice()

        if option == 'shoot':
            print(dedent("""
            You take a shot at the overseer member
            Miss
            The goon shoots at you and barely hits your arm. 
            You real back in pain and the Laxion takes a shot at him and he falls to the ground dead. 
            Your arm is pretty injured but still usable for now. Adrenaline is one hell of a drug.
            The captain looks at you and gives you a nod 
            you nod back just to acknowldge that you are okay and continue onto where the pod is.

            "Here I'm going to have to put you in with some cargo to disguise it. Each container has 
            an identifier chip on it so it should look like cargo has been launched and nothing 
            important buying you some time" 
            
            He pushes some cargo in there and pushes you along with it.
            
            "Once you hit the ground leave the landing site as soon as possible you will eventually be chased."
            you reply "If I get off this ship they might not let up"
            "why are they chasing you lad"
            "I have important information that could change the tide of this war"

            "I hope you get it into the right hands we'll be alright here but if my crew is at danger I will tell them that you got away."

            "Understood"

            you get into the pod with the cargo and Laxion enters the passcode to enter the ship and you get into the cockpit and blast off 

            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            """))
        
            return 'escape_ship'

        elif option == 'alert':
            print("captain gets shot in the arm")
            return 'pod'


class EscapeShip(Scene):
    def enter(self):
        print(dedent("""
        The pod detaches from the ouside hull of the ship and you take the controls and start 
        manueving the ship down looking for the nearest planet to land. The onboard 
        computer has 3 planets all in line 

        which planet do you choose <1> <2> OR <3>

        -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """))
        
        self.options = ['1', '2', '3']
        option = self.choice()
        
    
        if option == '1':
            print('work on this part')
            return 'escape_ship'

        elif option == '2':
            print("work on this part")
            return 'escape_ship'

        elif option == '3':
            print(dedent("""
            Seeing that the 3rd planet is closest and seems to have both water and trees due 
            to the colonization efforts that mankind has been pushing for the next few years.
            You set your sights and start to figure out how to get there. 
            There are ships flying all around still shooting at the freighter you have to manauver 
            through all of this to enter this unknown planet

            the route to the right is near the hull of the freighter and is being heavily fired at and the 
            route to your left is seemingly clear 

            which do you choose <right> or <left>
        

            --------------------------------------------------------------------------------------------------------------------------------------------------------------------
            """))

            self.options = ['right', 'left']
            option = self.choice()
            

            if option == 'right':
            #work on this one for later
                print("""
                you start veering towards the right which seems like a dangerous plan but the 
                ships start to pull away and go back to the left side where the Overseer attack ship is. 
                They seem to be unaware of your presense as you fly down to the mysterious planet
                """)

                print(dedent("""
                    You start to close in on this mysterious planet and the computers start yelling at you 
                    "-unidentified ship approaching-"

                    oh no 

                    you look at the rear cameras and see an overseer ship approaching fast 

                    you frantically make some inputs into the ship and make all the available shields go to he 
                    back of the ship just in time for a cannon shot 

                    BOOOOOM

                    sheilds are at half now if this little pod takes one more hit its down for the count

                    you take evasive manuavers and narrowly escape the second shot. The planet is closer now and 
                    you need to make sure you have enough protection for the entry. 
        
                    do you <move shields to the front> or keep <protecting the back>
                    -----------------------------------------------------------------------------------------------------------------------------------------------------------
                    """))

                self.options = ['move shields to the front', 'protecting the back']
                option = self.choice()

                if option == 'move shields to the front':
                    print(dedent("""
                    you move the shields to the fornt of the ship and veer to the right to narrowly avoid a third shot 
                    from the attack ship and entry begins. You have just enough sheilds to protect
                    you on entry through the mysterious planets atmosphere. 

                    The pods landing gear doesn't come out

                    you panick trying to manuever the ship to not crash straight into the woods. You veer upwards and 
                    try to avoid the trees but clip one and the ship starts crashing into the 
                    ground and you blackout 
                    
                    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    """))

                    return 'mysterious_planet'


            elif option == 'left':
                print(dedent("""
                    What was once clear is now full of enemy ships pulling back to the overseer attack ship and when they 
                    spot your ship they shoot it down instantly and you die in the firey explosion

                    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    """))

                return 'escape_ship'



class MysteriousPlanet(Scene):
    def enter(self):
        print(dedent("""
        Find out next time !!!!!!
        
        """))

        exit(1)