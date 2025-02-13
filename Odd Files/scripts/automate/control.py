import time
import pyautogui as ptg

class AutoControl:
    def __init__(self):
        pass

    #Display mouse position in real time
    def display_mouse_position(self):
        #ctrl c to stop operation
        while True:
            # Get current mouse position
            pos = ptg.position()
            print(f"Mouse position: {pos}", end="\r")  # Print on the same line
            time.sleep(0.1)  # Adjust the sleep time for smoother or faster updates

    #prints mouse position 
    def _printPos(self):
        pos = ptg.position() 
        print(pos)
        return pos

    #set mouse position per interval
    def controlMouse(self,Pos,interval):
        #moveTo() -> move to Pos
        ptg.moveTo(Pos,interval) #Pos in (x,y) tuple
        time.sleep(interval) #interval in secs

