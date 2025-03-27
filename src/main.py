import face_mesh as fm
import video
import mat
import cv2
import screen
import mouse

def drawEye( detection, frame, num_eye_in, num_eye_out, num_eye_pupil, move):

    detection.drawPoint(frame, num_eye_in)
    detection.drawPoint(frame, num_eye_out)
    detection.drawPoint(frame, num_eye_pupil)

    eye_in = detection.getPoint(num_eye_in)
    eye_out = detection.getPoint(num_eye_out)
    eye_pupil = detection.getPoint(num_eye_pupil)


    e1,e2,eye_center = mat.normalize(eye_in,eye_out,eye_pupil)


    eye_center *= 200
    eye_center.y += 100
    eye_center.x += 100 + move


    cv2.rectangle(frame, (move,0), (200+move,200), (255,255,255), -1)
    cv2.rectangle(frame, (move,0), (200+move,200), (0,0,0), 1)

    cv2.circle(frame, eye_center.get(), 0, (255,0,0), 40)

    #print(eye_pupil.z)


    #print((e1*200).get(),(e2*200).get(),(eye_center*200).get())

    #cv2.circle(frame, (e1*200+100).get(), 0, (255,0,0), 2)#blue
    #cv2.circle(frame, (e2*200+100).get(), 0, (0,255,0), 2)#green
    #cv2.circle(frame, (eye_center*200+100).get(), 0, (0,0,255), 2)#red



    return eye_center

def main():

    #cap = video.Video("temp/p.ogg")
    #cap = video.Video("temp/examaple.mp4")
    cap = video.Video(2)
    detection = fm.FaceMesh()
    monitor = screen.Screen()

    m = mouse.Mouse()

    while( cap.isOpened() ):
        
        frame = cap.getFrame()


        detection.detect(frame)

        #detection.drawEyeMask(frame)

        detection.drawMask(frame)
        

        eye_left_center = drawEye(detection, frame, 33, 133, 468,0)
        eye_right_center = drawEye(detection, frame, 463, 263, 473,200)


        m.moveTo(detection.getPoint(4))#nose

        
        video.showFrame(frame)
        #video.showFrame(monitor.getScreen())

        if ( cv2.waitKey(5) & 0xFF == ord('q') ):
            cap.release()
        


if __name__ == '__main__':
    main()
