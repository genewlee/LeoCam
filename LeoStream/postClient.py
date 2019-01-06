#!/usr/bin/env python

from datetime import datetime
from io import BytesIO
from picamera import PiCamera
from time import sleep
from requests import post
from subprocess import call

import base64
import os

def LeoCam_main():

    camera = PiCamera()
    camera.framerate = 32
    camera.resolution = (648, 486)
    camera.brightness = 55

    #give the sensor time to set its light levels
    sleep(1)

    while True:
        try:
            #timestamp
            now = str(datetime.now())

            stream = BytesIO()
    	    camera.capture(stream, format="jpeg")

            image_64_encode = base64.b64encode(stream.getvalue())
            data_for_js = "data:image/jpeg;base64,{}".format(image_64_encode)

            r = post("http://127.0.0.1:8080/" + now, data=data_for_js)

            if (r.status_code != 200):
                print(r.status_code, r.reason)
                break
        finally:
            stream.flush()

if __name__=='__main__':
    LeoCam_main()


