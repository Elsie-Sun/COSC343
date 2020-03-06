#!/usr/bin/env python3
from ev3dev2 . motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound
from time import sleep

cs = ColorSensor()
ts = TouchSensor()
sound = Sound()
drive = MoveTank(OUTPUT_B, OUTPUT_C)

# Stop program by long-pressing touch sensor button
while not ts.is_pressed:
    if cs.color == 1:
        sound.speak("Black")
        drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 2)
    elif cs.color == 6:
        sound.speak("White")
    sleep(1)
