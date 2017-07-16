#setup
import picamera
import time

#camera setup
camera = picamera.PiCamera()
timestr = time.strftime("%Y%m%d-%H%M%S")
print timestr
camera.resolution = (2592, 1944)
camera.start_preview()
#Camera warm up time
time.sleep(2)
camera.capture('%r.jpg') % timestr
