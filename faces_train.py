import os
import numpy as np
import cv2
from PIL import Image
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dir, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			print(label, path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id +=1

			id_ = label_ids[label]
			print(label_ids)
			#y_labels.append(label) #some number
			#x_train.append(path) #verify this image, turn into a NUMPY array, GRAY image
			pil_image = Image.open(path).convert("L") #grayscale
			image_array = np.array(pil_image, "uint8")
			#print(image_array)
			faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.5, minNeighbors = 5)

			for (x, y, w, h) in faces:
				roi = image_array[y: y+h, x: x+w]
				x_train.append(roi)
				#creating image id 
				y_labels.append(id_)

#print(y_labels)
#print(x_train)

with open("lables.pkl", "wb") as f:
	pickle.dump(label_ids, f)

#train the opencv recognizer
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
