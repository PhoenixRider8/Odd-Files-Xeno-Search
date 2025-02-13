import time
import pyautogui as ptg

class AutoType:
    #Above 3 functions put in DIFFERENT CLASS autoControl



    def openApp(self,app_name):
        ptg.press('win') #windows key
        ptg.write(app_name) #write notepad
        time.sleep(1)
        ptg.press('enter') #press Enter key

    def typeWrite(self,text):

        #OPEN NOTEPAD
        self.openApp('notepad')
        #TYPE MESSAGE
        time.sleep(1)
        ptg.write(text,interval=2)

    def paintEmoji(self,expression):
        self.openApp('paint')
        time.sleep(1)

        #expression
        distance = 200
        if(expression=="happy"):
            while distance > 0:
                #Face
                ptg.dragRel(distance,0, duration=0.2)
                ptg.dragRel(0,distance, duration=0.2)
                ptg.dragRel(-distance,0, duration=0.2)
                ptg.dragRel(0,-distance, duration=0.2)

                #Eyes
                ptg.dragRel(distance,distance/2, duration=0.2)
                distance = 0
        if(expression=="sad"):
            pass
        if(expression=="angry"):
            pass


    def cursorMaham(self):
        self.controlMouse((10,30),2)
        self.controlMouse((1700,60),2)
        self.controlMouse((600,90),2)