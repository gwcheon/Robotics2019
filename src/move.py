import time
import RPi.GPIO as GPIO
import click

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 14
Motor_A_Pin2  = 15
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

Dir_forward   = 0
Dir_backward  = 1

left_forward  = 0
left_backward = 1

right_forward = 0
right_backward= 1

pwn_A = 0
pwm_B = 0

def motorStop():#Motor stops
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():#Motor initialization
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    motorStop()
    try:
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass


def motor_right(status, direction, speed):#Motor 2 positive and negative rotation
    if status == 0: # stop
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor_B_EN, GPIO.LOW)
    else:
        if direction == Dir_backward:
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)
        elif direction == Dir_forward:
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)


def motor_left(status, direction, speed):#Motor 1 positive and negative rotation
    if status == 0: # stop
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor_A_EN, GPIO.LOW)
    else:
        if direction == Dir_forward:#
            GPIO.output(Motor_A_Pin1, GPIO.HIGH)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)
        elif direction == Dir_backward:
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.HIGH)
            pwm_A.start(0)
            pwm_A.ChangeDutyCycle(speed)
    return direction


def move(speed, direction, turn, radius=0.6):   # 0 < radius <= 1  
    if direction == 'forward':
        if turn == 'left':
            motor_left(0, left_backward, int(speed*radius))
            motor_right(1, right_forward, speed)
        elif turn == 'right':
            motor_left(1, left_forward, speed)
            motor_right(0, right_backward, int(speed*radius))
        else:
            motor_left(1, left_forward, 100)
            motor_right(1, right_forward, 100)
    elif direction == 'backward':
        if turn == 'left':
            motor_left(0, left_forward, int(speed*radius))
            motor_right(1, right_backward, speed)
        elif turn == 'right':
            motor_left(1, left_backward, speed)
            motor_right(0, right_forward, int(speed*radius))
        else:
            motor_left(1, left_backward, speed)
            motor_right(1, right_backward, speed)
    elif direction == 'no':
        if turn == 'left':
            motor_left(1, left_backward, 100)
            motor_right(1, right_forward, 100)
        elif turn == 'right':
            motor_left(1, left_forward, 100)
            motor_right(1, right_backward, 100)
        else:
            motorStop()
    else:
        pass


def destroy():
    motorStop()
    GPIO.cleanup()             # Release resource


if __name__ == '__main__':
    try:
        setup()

        speed = 50
        max_speed = 100
        min_speed = 0

        while True:
            key = click.getchar()
            if key == 'i':
                print('forward')
                move(speed, 'forward', '', 0)
                time.sleep(0.5)
            elif key == 'k':
                print('stop')
                move(0, 'backward', '', 0)
                time.sleep(0.5)
            elif key == 'm':
                print('backward')
                move(speed, 'backward', '', 0)
                time.sleep(0.5)
            elif key == 'j':
                print('left')
                move(speed, 'no', 'left', 0)
                time.sleep(0.5)
            elif key == 'l':
                print('right')
                move(speed, 'no', 'right', 0)
                time.sleep(0.5)
            elif key == 'w':
                if speed + 10 <= max_speed:
                    speed = speed + 10
                print('speed up:{0}'.format(speed))
            elif key == 'q':
                if speed - 10 >= min_speed:
                    speed = speed - 10
                print('speed down:{0}'.format(speed))

        
        #move(100, 'no', 1)
        #time.sleep(2.5)
        #move(-100, 'no', 1)
        #time.sleep(2.5)
        #move(100, 'left', 0.6)
        #time.sleep(5)
        print('1')
        
        #move(50, 'backward', 0.6)
        #time.sleep(1)
        #move(0, 'left', 1)
        #time.sleep(5)

    except KeyboardInterrupt:
        destroy()


