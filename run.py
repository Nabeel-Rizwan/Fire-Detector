from ultralytics import YOLO
import cvzone
import cv2
import math

# Running real time from webcam
cap = cv2.VideoCapture(0)       #   We can use external camera like CCTV to detect and monitor fire.
model = YOLO('fire.pt')         # Trained Model through Yolo

# Reading the classes
classnames = ['FIRE']

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(600,500))     # Frame size
    result = model(frame,stream=True)

    # Getting box,confidence and class names informations to work with. If confidence is more than 60 , It is a fire
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 60:
                x1,y1,x2,y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,500),5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100], scale=1,thickness=2)    # Text placement in frame




    cv2.imshow('frame',frame)
    cv2.waitKey(1)