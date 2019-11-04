#!/usr/bin/env python3
from gpiozero import Button, LED
import os
from signal import pause

powerPin = 26
powerenPin = 27
hold = 1
power = LED(powerenPin)
power.on()

def when_pressed():
  os.system("sudo pkill emulationstatio & openvt -c 1 -f clear && sudo omxplayer -b '/home/pi/RetroPie/splashscreens/RPz_off.mp4' && openvt -c 1 -f clear && sudo shutdown -h now")

btn = Button(powerPin, hold_time=hold)
btn.when_pressed = when_pressed
pause()
