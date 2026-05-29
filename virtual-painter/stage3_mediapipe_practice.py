import cv2
import mediapipe as mp

mp_drawing= mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        #COLOUR CONVERSION AND PRINTING LANDMARKS
        img=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result=hands.process(img)
        print(result.multi_hand_landmarks)
        img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
    
        #HAND LANDMARKS (loop added to consider more than one hand)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                print("index finger landmark:", hand_landmarks.landmark[8], ) #LANDMARK FOR TIP OF INDEX FINGER
        
        cv2.imshow("video", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


     
        