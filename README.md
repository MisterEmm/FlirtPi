# FlirtPi
A simple python script to play an internet radio steam on the Raspberry Pi and control the volume with 2x GPIO buttons.

The Flirt Pi is a simple, portable Raspberry Pi internet radio, that plays Soma FM, Secret Agent on startup using VLC media player. 

The project is fully documented at...

Instructables: https://www.instructables.com/id/1970-Flirt-Pi-Internet-Radio

Hackster: https://www.hackster.io/martin-mander/1970-flirt-pi-internet-radio-6f6fea

YouTube: https://youtu.be/d2tF_ky-CLA

...and all of my other projects are online at:

Instructables: https://www.instructables.com/member/MisterM/instructables/

Hackster: https://www.hackster.io/martin-mander/projects

YouTube: https://www.youtube.com/channel/UCRrwSKYBu4N7P6HWZsWJ2MA

Website: http://bit.ly/OldTechNewSpec

--------------------------------------------------------------------------

The flirt.py script is loaded on startup by the following method:

Edit the autostart file:

sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

and add in... 

@python3 /home/pi/flirt.py &

... as the last line. 

This instruction however will be ignored on startup if there's already a file at...

/home/pi/.config/lxsession/LXDE/autostart

... if that's the case edit this file, adding in the same line of code. 
