import cv2
import matplotlib as plt

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("photo.jpg",frame)
    cap.release()
    print(frame)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
take_photo()