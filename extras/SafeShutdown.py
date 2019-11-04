#!/usr/bin/env python3
from gpiozero import Button, LED
import os
from signal import pause

powerPin = 26
powerenPin = 27
hold = 1
power = LED(powerenPin)
power.on()

#functions that handle button events
#def when_pressed():
#  os.system("sudo fbi -T 2 -once -t 30 -noverbose -a '/home/pi/RetroPie/splashscreens/1.png &'")
#  os.system("sleep 5")
#  os.system("sudo killall emulationstation ; sleep 5s && sudo shutdown -h now")

#def when_pressed():
#  os.system("sudo killall emulationstation ; sudo fbi -T 2 -once -t 30 -noverbose -a '/home/pi/RetroPie/splashscreens/1.png' ; sleep 5 ; sudo shutdown -h now")

#def when_pressed():
#  os.system("sudo killall emulationstation & openvt -c 1 -f clear && sudo fbi -T 2 -once -t 30 -noverbose -a '/home/pi/RetroPie/splashscreens/1.png' ; sleep 5s && sudo shutdown -h now")

#def when_pressed():
#  os.system("sudo pkill emulationstatio & openvt -c 1 -f clear && sudo fbi -T 2 -once -t 30 -noverbose -a '/home/pi/RetroPie/splashscreens/1.png' ; sleep 5s && sudo shutdown -h now")

def when_pressed():
  os.system("sudo pkill emulationstatio & openvt -c 1 -f clear && sudo omxplayer -b '/home/pi/RetroPie/splashscreens/RPz_off.mp4' && openvt -c 1 -f clear && sudo shutdown -h now")

btn = Button(powerPin, hold_time=hold)
btn.when_pressed = when_pressed
pause()
