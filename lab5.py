import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)

#GPIO.setwarnings(False)
def Main()
	while True:
		for x in range(1,6):
			GPIO.output(11,1)
			time.sleep(0.5)
			GPIO.output(11,0)
			time.sleep(0.5)

if __name__ == '__main__':
	Main():