import cv2
import os

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.	COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for i, (x, y, w, h) in enumerate(faces):
    	print(x, y, w, h)
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = frame[y:y+h, x:x+w]

    	#recognizer? deep learned model
    	
    	img_item = "my_image.png"
    	#roi = region of interest
    	cv2.imwrite(img_item, roi_gray)

    	#make rectangle
    	color = (255, 0, 0) #BGR
    	stroke = 2
    	end_cord_x = x + w
    	end_cord_y = y + h
    	cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    	if(i == 5): break

    
    #Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
        
#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()