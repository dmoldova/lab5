import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)

#GPIO.setwarnings(False)

while True:
	for x in range(1,6):
		GPIO.output(13,1)
		time.sleep(0.5)
		GPIO.output(13,0)
		time.sleep(0.5)