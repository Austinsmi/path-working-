# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""

import binascii#binascii imports libraries that we need
import board
import busio
import digitalio
import time

from dabble import Dabble # imports the librraries that we need

dabble = Dabble(board.GP0, board.GP1, debug=True) #Ataches it to a  gp and turns it on

import pwmio


from adafruit_motor import motor  # inports a small amount of the  adifruit_motor line

right_motor_forward = (board.GP14)  # initilize the varable right_mortor fowards and attaches it to gp 12
right_motor_backward = (board.GP15)  # initilize the varable right_mortor backwards  and attaches it to gp 13

pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000)  # tells the pico tht it is an component it is an output
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)  # tells the pico tht it is an component it is an output


left_motor_forward = board.GP12
left_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)  # configurtion line is needed initilizes left motor
Left_Motor_speed = 0  # Initilizes left_motor_forward spped to 0

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0


def forwards():
    Left_Motor_speed = 1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1  # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def backwards():
    Left_Motor_speed = -1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1  # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def turn_left():
    Left_Motor_speed = -1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def turn_right():
    Right_Motor_speed = -1 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def Stop():
    Right_Motor_speed = 0 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 0  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed


while True:
    message = dabble.read_message() #commands to take from th buethooth Module.
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            print("Move both motors forward")
            forwards()
        elif (message.down_arrow_pressed):
            print("Move both motors backward")
            backwards()
        elif (message.right_arrow_pressed):
            print("Move left motor forward and right motor backward")
            turn_right()
        elif (message.left_arrow_pressed):
            print("Move left motor backward and right motor forward")
            turn_left()
        elif (message.no_direction_pressed):
            print("Stop both motors")
            Stop()
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
# Write your code here :-)
