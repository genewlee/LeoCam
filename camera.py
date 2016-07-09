from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.start_preview()
camera.rotate = 180
sleep(5)
now = datetime.now()[:19]
camera.capture('/home/pi/Desktop/%s.jpg' % str(now))
camera.stop_preview()
