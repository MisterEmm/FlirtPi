#!/bin/python
from gpiozero import Button
from signal import pause
from subprocess import Popen
import vlc

media = vlc.MediaPlayer('http://ice4.somafm.com/secretagent-128.mp3')

def increase_volume():
    change_volume('+')
    print("Volume Up")

def decrease_volume():
    change_volume('-')
    print("Volume Down")

def change_volume(ch_sign):
    Popen(['amixer', 'set', 'Master', 'unmute'])
    Popen(['amixer', 'set', 'Master', '5%{}'.format(ch_sign)])

def mute_volume():
    Popen(['amixer', 'set', 'Master', 'mute'])
    
media.play()
 
button_up = Button(5)
button_up.when_pressed = increase_volume
button_down = Button(7)
button_down.when_pressed = decrease_volume
button_down.when_held = mute_volume
pause()