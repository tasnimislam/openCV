import cv2
import os
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("lables.pkl", "rb") as f:
	og_labels = pickle.load(f)
	labels = {v:k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.	COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for i, (x, y, w, h) in enumerate(faces):
    	#print(x, y, w, h)
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = frame[y:y+h, x:x+w]

    	#recognizer? deep learned model
    	id_, conf = recognizer.predict(roi_gray)
    	if conf<100:
    		print(id_)
    		print(labels[id_])

    		

    	img_item = "my_image.png"
    	#roi = region of interest

    	#make rectangle
    	color = (255, 0, 0) #BGR
    	stroke = 2
    	end_cord_x = x + w
    	end_cord_y = y + h
    	cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    	cv2.putText(frame, "dead soul:" + str(conf), (x, y + 30),cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
    	cv2.imwrite(img_item, frame)

    	

    
    #Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
        
#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()