import RPI.GPIO as GPIO
import time
GPIO.setmode(GRPIO.BOARD)

GPIO.setup(17, GPIO.OUT)

while True:
	for x in range(1,6):
		GPIO.out(17,True)
		time.sleep(0.5)
	