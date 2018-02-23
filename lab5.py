import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

while True:
	for x in range(1,6):
		GPIO.out(11,True)
		time.sleep(0.5)
	
