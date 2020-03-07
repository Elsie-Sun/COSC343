#!/usr/bin/env python3
from ev3dev2 . motor import *
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from time import sleep

cl = ColorSensor()
cl.mode = 'COL-COLOR'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

count = 0
sound = Sound()

mB.run_forever(speed_sp=150)
mC.run_forever(speed_sp=150)

while cl.color == 1:
    count += 1
    if count == 1:
        mB.run_to_rel_pos(position_sp=340, speed_sp=200, stop_action="brake")
        sound.speak(count)

    sound.speak(count)

    mB.wait_while('running')
    mC.wait_while('running')





