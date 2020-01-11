import RPi.GPIO as GPIO
import sys
import time
import Adafruit_PCA9685
import os
import click

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

motor_pos = [100, 245, 100, 100, 100]
motor_id  = 0

while True:
    key = click.getchar()
    if key == 'q':
        print("Terminated app")
        break
    elif key == '1': # camera
        motor_id = 1
        print('servo#1 selected')
    elif key == '2': # robot-arm#1 lower arm
        motor_id = 2
        print('servo#2 selected')
    elif key == '3': # robot-arm#2 middle arm
        motor_id = 3
        print('servo#3 selected')
    elif key == '4': # robot-arm#3 rotating arm
        motor_id = 4
        print('servo#4 selected')
    elif key == '5': # robot-arm#4 gripper
        motor_id = 5
        print('servo#5 selected')
    elif key == 'o': # increase
        if motor_id > 0 and motor_id < 6:
            motor_pos[motor_id - 1] += 5
            print('motor#{0}.value={1}'.format(motor_id, motor_pos[motor_id - 1]))
            pwm.set_pwm(motor_id + 10, 0, motor_pos[motor_id - 1])
        else:
            print('Select motor first')
    elif key == 'p': # decrease
        if motor_id > 0 and motor_id < 6:
            motor_pos[motor_id - 1] -= 5
            print('motor#{0}.value={1}'.format(motor_id, motor_pos[motor_id - 1]))
            pwm.set_pwm(motor_id + 10, 0, motor_pos[motor_id - 1])
        else:
            print('Select motor first')
    else:
        print('invalid key input')

'''
pos = 220
for i in range(12):
    pwm.set_pwm(12, 0, pos)
    pos += 10
    time.sleep(0.1)

time.sleep(1)
'''
