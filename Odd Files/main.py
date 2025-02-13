import pygame as pg
import sys
from scripts.scenes.game import Game
from scripts.scenes.scene1 import Scene1
from scripts.scenes.scene2 import Scene2
from scripts.scenes.scene3 import Scene3
from scripts.scenes.scene4 import Scene4
from scripts.scenes.scene5 import Scene5

from scripts.scenes.transition import Transition
from scripts.music.musicPlayer import Music

#GAME ICON
pygame_icon = pg.image.load('assets/icons/xeno.jpg')
pg.display.set_icon(pygame_icon)

#GAME MUSIC
mS = Music()

# GAME LAUNCHES HERE
g = Game()
pg.display.set_caption("ODD FILES")
# MAIN MENU : 
#mainMenu music
mS.pickMusic("mainMenu")
mS.play()

while g.menuRunning:
    g.mainMenu(g.canvas)
    g.handle_menu_clicks()  # Check for button clicks in the menu
    g.menu()

#Scene 1
s1 = Scene1(g.screen,g.clock)
s1.sceneRunning = True
s1.dialogue_system.start_dialogue()
#dialogue music
mS.pickMusic("dialogue")
mS.play()
while s1.scene1Playing:
    s1.main2()

# GAME RUNNING
g.dialogue_system.start_dialogue()
g.running = True  # Change it when the button function is added
#dialogue music
mS.pickMusic("dialogue")
mS.play()
while g.running:
    g.main()
    #g.game_over()
print("TIME TO SEARCH")

#Scene 2
s2 = Scene2(g.screen,g.clock)
s2.scene1Playing = True
s2.dialogue_system.start_dialogue()
#mainMenu music
mS.pickMusic("mainMenu")
mS.play()
while s2.scene1Playing:
    s2.main2()

print("Transition scene")
#Transition
t = Transition(g.screen,g.clock)
t.transitionPlaying = True
while t.transitionPlaying:
    t.main2()


'''---------------------------------------------------------------------------------------------------------------------------'''









#BOSSES

'''VIRUSSSSSSSSSSSSSSSSSSSSSSSSS'''
#VIRUS
#virus music
mS.pickMusic("virus")
mS.play()
s3 = Scene3(g.screen,g.clock)
s3.virusPlaying = True
while s3.virusPlaying:
    s3.main()

'''---------------------------------------------------------------------------------------------------------------------------'''

print("Transition scene")
#Transition
t = Transition(g.screen,g.clock)
t.transitionPlaying = True
while t.transitionPlaying:
    t.main2()

'''MICCCCCCCCEEEEEEEEEEEEEEEEEEEEE'''

#MICE
#mice music
mS.pickMusic("mice")
mS.play()
s4 = Scene4(g.screen,g.clock)
s4.micePlaying = True
while s4.micePlaying:
    s4.main()

'''---------------------------------------------------------------------------------------------------------------------------'''

print("Transition scene")
#Transition
t = Transition(g.screen,g.clock)
t.transitionPlaying = True
while t.transitionPlaying:
    t.main2()

'''JOKKEEEEEEERRRRRRRRRRRR'''

#JOKER
#joker music
mS.pickMusic("joker")
mS.play()
s5 = Scene5(g.screen,g.clock)
s5.jokerPlaying = True
while s5.jokerPlaying:
    s5.main()

'''---------------------------------------------------------------------------------------------------------------------------'''

print("Transition scene")
#Transition
t = Transition(g.screen,g.clock)
t.transitionPlaying = True
while t.transitionPlaying:
    t.main2()

'''BACK TO MAIN MENU'''

#Back to main menu
#dialogue music
mS.pickMusic("mainMenu")
mS.play()
g.menuRunning = True
while g.menuRunning:
    g.mainMenu(g.canvas)
    g.handle_menu_clicks()  # Check for button clicks in the menu
    g.menu()

#Quit Game
pg.quit()
sys.exit()
