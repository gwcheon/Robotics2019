import RPi.GPIO as GPIO
import sys
import time
import Adafruit_PCA9685
import os
import click

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

motor_pos = [300, 240, 300, 160, 300]
motor_pos_max = [300, 400, 330, 250, 320]
motor_pos_min = [200, 200, 250, 100, 220]
motor_dpos = 4
motor_id  = 0

# position init
pwm.set_pwm(11, 0, motor_pos[0])
pwm.set_pwm(12, 0, motor_pos[1])
pwm.set_pwm(13, 0, motor_pos[2])
pwm.set_pwm(14, 0, motor_pos[3])
pwm.set_pwm(15, 0, motor_pos[4])

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
            if motor_pos[motor_id - 1] + motor_dpos <= motor_pos_max[motor_id - 1]:
                motor_pos[motor_id - 1] += motor_dpos
            print('motor#{0}.value={1}'.format(motor_id, motor_pos[motor_id - 1]))
            pwm.set_pwm(motor_id + 10, 0, motor_pos[motor_id - 1])
        else:
            print('Select motor first')
    elif key == 'p': # decrease
        if motor_id > 0 and motor_id < 6:
            if motor_pos[motor_id - 1] - motor_dpos >= motor_pos_min[motor_id - 1]:
                motor_pos[motor_id - 1] -= motor_dpos
            print('motor#{0}.value={1}'.format(motor_id, motor_pos[motor_id - 1]))
            pwm.set_pwm(motor_id + 10, 0, motor_pos[motor_id - 1])
        else:
            print('Select motor first')
    else:
        print('invalid key input')


