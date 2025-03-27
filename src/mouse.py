import pyautogui

class Mouse:

    def __init__(self):
        self.screenW = 1024
        self.screenH = 1024
    
    def moveTo(self,p):
        x = p.x
        y = p.y
        x = int(x*self.screenW)
        y = int(y*self.screenH)
        pyautogui.moveTo(x,y)