import RPi.GPIO as GPIO
import sys
import time
import Adafruit_PCA9685
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    '''
    r[r < 2 * b] = 0
    r[r < 2 * g] = 0
    frame_copy = np.zeros(frame.shape)
    frame_copy[:,:,0] = np.zeros(b.shape)
    frame_copy[:,:,1] = np.zeros(g.shape)
    frame_copy[:,:,2] = r
    '''
    
    #edge = cv2.Canny(gray, 100, 200)

    blur = cv2.GaussianBlur(gray, (11,11), cv2.BORDER_DEFAULT)

    cv2.imshow('display', blur)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

