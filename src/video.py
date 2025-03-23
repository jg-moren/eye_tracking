import cv2

FRAME_SIZE = (640, 480)
#FRAME_SIZE = (320, 240)
#FRAME_SIZE = (800, 800)

def showFrame( frame ):
    frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
    frame = cv2.flip(frame,1)
    cv2.imshow('img',frame)

class Video:

    def __init__(self, source):
        self.capture = cv2.VideoCapture( source )

        #capture.set(cv2.CAP_PROP_FPS, 30.0)
        #capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_SIZE[0])
        #capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_SIZE[1])

        width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.capture.get(cv2.CAP_PROP_FPS))

        print(f"Source({source}), fps: {fps}, resolution: {width} x {height}")


    def getFrame( self ):
        ok, frame = self.capture.read()
        #frame = frame[0:int(frame.shape[0]*0.5),int(frame.shape[1]*0.3):int(frame.shape[1]*0.7) ]
        #frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
        return frame    

    
    def isOpened(self):
        return self.capture.isOpened()
    

    def release(self):
        self.capture.release()