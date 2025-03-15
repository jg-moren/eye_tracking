import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

class FaceMesh:


    def __init__(self):


        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        
        self.result = False

    def detect(self, image):

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        res = self.face_mesh.process(image)

        if res.multi_face_landmarks:
            self.result = res 
        
        
    
    def drawPoint(self, image, point):
        if not self.result:
            return


        coo = self.result.multi_face_landmarks[0].landmark[point]

        point = (int(coo.x * image.shape[1]), int(coo.y * image.shape[0]))

        cv2.circle(image, point, 0, (255,0,0), 5)

    def getPoint(self, point):
        if not self.result:
            return (0,0)
        return self.result.multi_face_landmarks[0].landmark[point]


    def drawMask(self, image):
        #image.flags.writeable = True
        
        if self.result.multi_face_landmarks:
            for face_landmarks in self.result.multi_face_landmarks:
                con = frozenset().union(*[
                    mp_face_mesh.FACEMESH_RIGHT_IRIS, 
                    mp_face_mesh.FACEMESH_LEFT_IRIS,
                    mp_face_mesh.FACEMESH_RIGHT_EYE,
                    mp_face_mesh.FACEMESH_LEFT_EYE
                ])
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=con,#mp_face_mesh.FACEMESH_RIGHT_IRIS,
                    landmark_drawing_spec=None
                )
        return image
       