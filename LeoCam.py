#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
from datetime import datetime

from DropBoxAgent import DropBoxAgent

from sys import argv
from subprocess import call

def LeoCam_main():

    photo = True

    if len(argv) < 2:
        print "usage: {} <video | photo>".format(argv[0])
        exit(1)
    
    if argv[1] == 'video':
        photo = False
    
    camera = PiCamera()
    camera.framerate = 15
    if photo:
        camera.resolution = (2592, 1944)

    #give the sensor time to set its light levels
    sleep(5)

    #timestamp
    now = datetime.now()
    now = str(now)[:19]

    filepath = '/home/pi/Desktop/LeoCam_captures/%s.h264' % now
    if photo:
        filepath = '/home/pi/Desktop/LeoCam_captures/%s.jpg' % now

    if photo: #take picture
        camera.capture(filepath)
    else: # record
        camera.start_recording(filepath)
        sleep(5) # 5 second photo
        camera.stop_recording()

        call(["cd /home/pi/Desktop/LeoCam_captures",
              "ffmpeg -r 30 -i" + "{} -vcodec copy {}.mp4".format(filepath, filepath.split('.')[0])])

    LeoClient = DropBoxAgent()

    LeoClient.upload(filepath)

if __name__=='__main__':
    LeoCam_main()
