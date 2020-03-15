#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import *
from time import sleep, time
from ev3dev2.sensor.lego import ColorSensor, SoundSensor

cl = ColorSensor()
cl.mode = 'COL-COLOR'
sou = Sound()
count = 0
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while cl.value() == 1:
    count += 1
    mB.run_to_rel_pos(position_sp=0.6, speed_sp=50, stop_action="brake")

sou.speak(count)

