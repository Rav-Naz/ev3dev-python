#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (LightSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from random import randint
from time import sleep


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

direction = "NONE"
pointing = False

# Initialize the motors.
left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
arm_motor = Motor(Port.A)
arm_motor.reset_angle(0)
line_sensor = LightSensor(Port.S1)

sensor_center = UltrasonicSensor(Port.S2)
sensor_left = InfraredSensor(Port.S3)
sensor_right = InfraredSensor(Port.S4)

# Initialize the drive base.
arm_motor.run_angle(200,120)
robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=125)
robot.settings(500,500,500,500)

def outOfBounds():
    if line_sensor.reflection() > 40:
        robot.straight(80)
        # arm_motor.run_angle(500,30)
        robot.reset()
        robot.turn(-280)
        # arm_motor.run_angle(500,-30)


def scanSensor(): # 1-left, 2-center, 3-right
    degree = 0.0
    offset = 60
    distance_center = sensor_center.distance() #in mm
    distance_left = sensor_left.distance() #in percent
    distance_right = sensor_right.distance() #in percent

    if(distance_center>500):
        pointing = False
        if(distance_left<offset):
            degree = 90*(offset/distance_left)
        elif(distance_right<offset):
            degree = -90*(offset/distance_right)

        if(degree>offset):
            robot.turn(offset)
            # degree = degree - offset
        elif(degree<-offset):
            robot.turn(-offset)
            # degree = degree + offset
    else:
        pointing = False
    return degree

ev3.speaker.beep()

while True:
    if Button.LEFT in ev3.buttons.pressed():
        direction = "LEFT"
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep(frequency=1000, duration=100)
        robot.turn(-200)
        arm_motor.run_angle(200,-120)
        break
    elif Button.RIGHT in ev3.buttons.pressed():
        direction = "RIGHT"
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep()
        sleep(1)
        ev3.speaker.beep(frequency=1000, duration=100)
        robot.turn(200)
        arm_motor.run_angle(200,-120)
        break

while True:
    if direction != "NONE":
        robot.drive(-(400 if pointing else 200),scanSensor())
        outOfBounds()