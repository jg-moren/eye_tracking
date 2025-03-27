import pyautogui
import numpy as np
import mat

class Mouse:

    def __init__(self):

        img = pyautogui.screenshot()
        frame = np.array(img)
        self.screenHeight = frame.shape[0]
        self.screenWight = int(frame.shape[1]/2)

        self.mouse = mat.dot(pyautogui.position() )
    
    def moveTo(self,p):
        if( p == (0,0) ):
            return
        x = int((1-p.x)*self.screenWight)
        y = int(p.y*self.screenHeight)
        point = mat.dot((x,y))


        #print(point.get())

        if( mat.dist(point, self.mouse) >= 3 ):
            pyautogui.moveTo(point.x,point.y,0)
            self.mouse = point
