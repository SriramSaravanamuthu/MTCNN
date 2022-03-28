import cv2
import os
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

video = cv2.VideoCapture(0)

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
confidence = 0.7

while video.isOpened():
    print('1')
    ret,frame = video.read()
    if ret == True:
        print('2')
        rgb_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb_image)
        
        for face in faces:
            print('3')
            
            if face['confidence'] >= confidence:
                x,y,w,h = face['box']
                print('writing frame..')
                img = frame[y:y+h,x:x+w]
            cv2.imshow('frame',img)
        
        
        
        
    if cv2.waitKey(10)==ord('q'):
        cv2.destroyAllWindows()
        video.release()
        test.release()
        break