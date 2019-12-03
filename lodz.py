#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1,INPUT_2
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

tsL = TouchSensor(INPUT_1) #Przycisk na wysięgniku lewym
tsR = TouchSensor(INPUT_2) #Przycisk na wysięgniku prawym

rgb = ColorSensor(INPUT_3) #Czujnik koloru

mLT = LargeMotor(OUTPUT_A) #Silnik lewy tylny
mLP = LargeMotor(OUTPUT_B) #Silnik lewy przedni
mRT = LargeMotor(OUTPUT_C) #Silnik prawy tylny
mRP = LargeMotor(OUTPUT_D) #Silnik prawy przedni

def motorOnSeconds(LEFT_SECONDS,RIGHT_SECONDS,POWER):
    "Do poruszania silnikami przez czas SECONDS o mocy POWER"
    mLT.on_for_seconds(SpeedPercent(POWER), LEFT_SECONDS)
    mLP.on_for_seconds(SpeedPercent(POWER), LEFT_SECONDS)
    mRT.on_for_seconds(SpeedPercent(POWER), RIGHT_SECONDS)
    mRP.on_for_seconds(SpeedPercent(POWER), RIGHT_SECONDS)

def motorOnRotations(LEFT_ROTATIONS,RIGHT_ROTATIONS,POWER):
    mLT.on_for_seconds(SpeedPercent(POWER), LEFT_ROTATIONS)
    mLP.on_for_seconds(SpeedPercent(POWER), LEFT_ROTATIONS*1.666667)
    mRT.on_for_seconds(SpeedPercent(POWER), RIGHT_ROTATIONS)
    mRP.on_for_seconds(SpeedPercent(POWER), RIGHT_ROTATIONS*1.666667)
    

while True:
    if ts.is_pressed:
        for i in range(1,51):
            print(i)
            
            
        # leds.set_color("LEFT", "GREEN")
        # leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")