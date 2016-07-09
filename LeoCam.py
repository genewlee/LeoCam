#!/usr/bin/python

from picamera import PiCamera
from time import sleep
from datetime import datetime

from DropBoxAgent import DropBoxAgent

def LeoCam_main():
    
    camera = PiCamera()

    #give the sensor time to set its light levels
    sleep(5)

    #timestamp
    now = datetime.now()
    now = str(now)[:19]

    filepath = '/home/pi/Desktop/LeoCam_captures/%s.jpg' % now

    #take picture
    camera.capture(filepath)

    LeoClient = DropBoxAgent()

    LeoClient.upload(filepath)

if __name__=='__main__':
    LeoCam_main()