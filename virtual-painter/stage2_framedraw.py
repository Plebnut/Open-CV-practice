import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

img2 = cv2.line(img, (250,150), (330,330), (255,0,0), 3)
img3 = cv2.rectangle(img, (250,250), (450,450), (0,250,0), 3)
img4 = cv2.circle(img, (300,300), 100, (0,0,255),4, cv2.FILLED)

cv2.imshow("black image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()