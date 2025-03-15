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
    frame = cv2.flip(frame,1)
    cv2.imshow('img',frame)

def getEye( detection, frame, num_eye_in, num_eye_out, num_eye_pupil ):
    detection.drawPoint(frame, num_eye_in)
    detection.drawPoint(frame, num_eye_out)
    detection.drawPoint(frame, num_eye_pupil)
    
    eye_in = detection.getPoint(num_eye_in)
    eye_out = detection.getPoint(num_eye_out)
    eye_pupil = detection.getPoint(num_eye_pupil)

    _,_,eye_center = mat.normalize(eye_in,eye_out,eye_pupil)

    return eye_center

def main():

    #cap = getCapture("temp/examaple.mp4")
    cap = getCapture(2)

    detection = fm.FaceMesh()

    while( cap.isOpened() ):
        
        frame = getFrame(cap)

        detection.detect(frame)

        #detection.drawMask(frame)

        eye_left_center = getEye(detection, frame, 33, 133, 468)
        eye_right_center = getEye(detection, frame, 463, 263, 473)

        eye_left_center *= 200
        eye_left_center.y += 100

        eye_right_center *= 200
        eye_right_center.y += 100
        eye_right_center.x += 100


        cv2.circle(frame, (100,100), 0, (255,0,0), 100)
        cv2.circle(frame, (200,100), 0, (255,0,0), 100)
        
        cv2.circle(frame, eye_left_center.get(), 0, (255,255,255), 20)
        cv2.circle(frame, eye_right_center.get(), 0, (255,255,255), 20)

        
        showFrame(frame)


        if ( cv2.waitKey(5) & 0xFF == ord('q') ):
            cap.release()
        


if __name__ == '__main__':
    main()
