import RPi.GPIO as GPIO
import time

Tr = 11
Ec = 8

def checkdist():       #Reading distance
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):
        pass
    t1 = time.time()
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

if __name__ == "__main__":
    try:
        while True:
            dist = checkdist()
            print(dist)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

