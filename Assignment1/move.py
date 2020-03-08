#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from time import sleep

## sensors
cl = ColorSensor()
cl.mode = 'COL-COLOR'

sound = Sound()
gy = GyroSensor() # not used now

## controls robot
drive = MoveTank(OUTPUT_B, OUTPUT_C)
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# count how many black tiles the robot passed
count = 0


while True:
    if count < 1:
        drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 0.6)

    # detects a black tile
    if cl.color == 1:
        count += 1
        if count == 1:
            mB.run_to_rel_pos(position_sp=340, speed_sp=360, stop_action="brake")
            sound.speak(count)
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 0.5)
        elif 1 < count < 7:
            sound.speak(count)
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 1.2)
        elif count == 7:
            mB.run_to_rel_pos(position_sp=340, speed_sp=360, stop_action="brake")
            sound.speak(count)
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 2.1)
        elif 7 < count < 13:
            sound.speak(count)
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 2.1)
        elif count == 13:
            mC.run_to_rel_pos(position_sp=340, speed_sp=360, stop_action="brake")
            sound.speak(count)

    # do not detect a black tile
    # move back and correct its position(not complete)
    elif cl.color != 1:
        if count < 7:
            count -= 1
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), -1.2)

        elif 7 < count < 13:
            count -= 1
            drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), -2.1)

sleep(2)
