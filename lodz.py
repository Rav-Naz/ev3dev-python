#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor,UltrasonicSensor
from ev3dev2.button import Button
import os
from time import sleep
from random import randint

os.system('setfont Lat15-TerminusBold14')
tsL = TouchSensor(INPUT_4) #Przycisk na wysięgniku lewym
tsP = TouchSensor(INPUT_3) #Przycisk na wysięgniku prawym

ultra = UltrasonicSensor(INPUT_1)
button = Button()

mLT = LargeMotor(OUTPUT_A) #Silnik lewy tylny
mLP = LargeMotor(OUTPUT_B) #Silnik lewy przedni
mRT = LargeMotor(OUTPUT_C) #Silnik prawy tylny
mRP = LargeMotor(OUTPUT_D) #Silnik prawy przedni

light = LightSensor(INPUT_2) #Czujnik koloru

def Rotate(POWER, TIME=.250):
    mLT.run_forever(speed_sp=-POWER)
    mLP.run_forever(speed_sp=(-POWER/1.667))
    mRT.run_forever(speed_sp=POWER)
    mRP.run_forever(speed_sp=(POWER/1.667))
    sleep(TIME)
    mLP.stop()
    mLT.stop()
    mRT.stop()
    mRP.stop()

def motorOnRotations(LEFT_ROTATIONS,RIGHT_ROTATIONS,POWER):
    mLT.on_for_rotations(SpeedPercent(POWER), LEFT_ROTATIONS)
    mLP.on_for_rotations(SpeedPercent(POWER), LEFT_ROTATIONS*1.666667)
    mRT.on_for_rotations(SpeedPercent(POWER), RIGHT_ROTATIONS)
    mRP.on_for_rotations(SpeedPercent(POWER), RIGHT_ROTATIONS*1.666667)

def motorRunForever(POWER):
    mLT.run_forever(speed_sp=-POWER)
    mLP.run_forever(speed_sp=(-POWER/1.667))
    mRT.run_forever(speed_sp=-POWER)
    mRP.run_forever(speed_sp=(-POWER/1.667))

while True:

    if button.down:
        sleep(5)
        Rotate(-1050, .200)
        Rotate(1050, 1.200)
        break

    elif button.enter:
        sleep(5)
        Rotate(1050, .200)
        Rotate(-1050, .500)
        break

motorRunForever(1050)

while True:
    if light.reflected_light_intensity > 60:
        rand = randint(0,1)
        if rand == 0:
            Rotate(-1050, 1)
        elif rand == 1:
            Rotate(-1050, 1)
        motorRunForever(1050)

    elif tsL.is_pressed:
        Rotate(-1050, .5)
        motorRunForever(1050)

    elif tsP.is_pressed:
        Rotate(1050, .5)
        motorRunForever(1050)

    try:
        if ultra.distance_centimeters_ping <= 5:
            break
        elif ultra.distance_centimeters_ping <= 10:
            motorRunForever(1050)
        elif ultra.distance_centimeters_ping <= 30:
            rand = randint(0,1)
            if rand == 0:
                Rotate(-1050,.4)
            elif rand == 1:
                Rotate(-1050,.4)
            motorRunForever(1050)
    except:
        pass