import cv2
import face_mesh as fm
import mat

FRAME_SIZE = (640, 480)
#FRAME_SIZE = (320, 240)
#FRAME_SIZE = (800, 800)


def getCapture( source ):
    capture = cv2.VideoCapture( source )

    #capture.set(cv2.CAP_PROP_FPS, 30.0)
    #capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_SIZE[0])
    #capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_SIZE[1])

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    print(f"Source({source}), fps: {fps}, resolution: {width} x {height}")

    return capture


def getFrame( cap ):
    ok, frame = cap.read()
    frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
    return frame    


def showFrame( frame ):
    frame = cv2.resize(frame, (FRAME_SIZE), interpolation=cv2.INTER_LANCZOS4)
    #frame = cv2.flip(frame,1)
    cv2.imshow('img',frame)


def main():

    #cap = getCapture("temp/examaple.mp4")
    cap = getCapture(2)

    detection = fm.FaceMesh()

    while( cap.isOpened() ):
        
        frame = getFrame(cap)

        detection.detect(frame)

        #detection.drawMask(frame)

        detection.drawPoint(frame, 33)
        detection.drawPoint(frame, 133)
        detection.drawPoint(frame, 468)
        
        
        p1 = detection.getPoint(33)
        p2 = detection.getPoint(133)
        p3 = detection.getPoint(468)
        
        p4,p5,p6 = mat.normalize(p1,p2,p3)
        p4 = p4 * 200
        p5 = p5 * 200
        p6 = p6 * 200

        cv2.circle(frame, p4.get(), 0, (255,0,0), 8)
        cv2.circle(frame, p5.get(), 0, (255,0,0), 8)
        cv2.circle(frame, p6.get(), 0, (255,0,0), 8)
        cv2.rectangle(frame, (0,0), (200,200), (255,0,0), 8)
        
        showFrame(frame)


        if ( cv2.waitKey(5) & 0xFF == ord('q') ):
            cap.release()
        


if __name__ == '__main__':
    main()
