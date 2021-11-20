#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor,UltrasonicSensor
from ev3dev2.button import Button
import os
from time import sleep
from random import randint, choice
from ev3dev2.led import Leds

os.system('setfont Lat15-TerminusBold14')

ultra = UltrasonicSensor(INPUT_1)

# mLT = LargeMotor(OUTPUT_A) #Silnik lewy tylny
# mLP = LargeMotor(OUTPUT_B) #Silnik lewy przedni
# mRT = LargeMotor(OUTPUT_C) #Silnik prawy tylny
# mRP = LargeMotor(OUTPUT_D) #Silnik prawy przedni

ramie = LargeMotor(OUTPUT_A);
napedLewy = LargeMotor(OUTPUT_C);
napedPrawy = LargeMotor(OUTPUT_D);

light = LightSensor(INPUT_2) #Czujnik koloru

leds = Leds()

button = Button()

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

idleSpeed = 650
attackSpeed = 1050

baseDegrees = .950

def outOfBounds():
    if light.reflected_light_intensity > 60:
        rand = randint(0,1)
        motorRunForever(-attackSpeed)
        sleep(.4)
        if rand == 0:
            Rotate(attackSpeed, .5)
        elif rand == 1:
            Rotate(-attackSpeed, .5)
        motorRunForever(idleSpeed)
        return True
    return False

while True:

    leds.set_color("LEFT", "RED")
    leds.set_color("RIGHT", "RED")

    if tsP.is_pressed:
        rand = choice((-1,1))
        sleep(5)
        Rotate(-attackSpeed, .200)
        Rotate(attackSpeed, baseDegrees+rand*.100)
        break

    elif tsL.is_pressed:
        rand = choice((-1,1))
        sleep(5)
        Rotate(attackSpeed, .200)
        Rotate(-attackSpeed, baseDegrees+rand*.100)
        break

motorRunForever(attackSpeed)

skan = True

while True:
    if button.enter:
        break
    wart = ultra.distance_centimeters
    if outOfBounds():
        continue

    elif tsL.is_pressed:
        skan = True
        Rotate(-attackSpeed, .5)
        motorRunForever(attackSpeed)

    elif tsP.is_pressed:
        skan = True
        Rotate(attackSpeed, .5)
        motorRunForever(attackSpeed)


   # if outOfBounds():
    #    continue

    elif wart <= 20:
        motorRunForever(attackSpeed)
        skan = True

    elif wart <= 55  and wart >= 30 and skan:
        rand = randint(0,1)
        if rand == 0:
            Rotate(-attackSpeed,.15)
        elif rand == 1:
            Rotate(attackSpeed,.15)
        motorRunForever(idleSpeed)
        skan = False