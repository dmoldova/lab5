import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 11

GPIO.setup(led,GPIO.OUT)

#GPIO.setwarnings(False)
def Main():
	while True:
		for x in range(1,6):
			GPIO.output(led,1)
			time.sleep(0.5)
			GPIO.output(led,0)
			time.sleep(0.5)

if __name__ == '__main__':
	Main()