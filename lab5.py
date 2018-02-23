import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led = 11

GPIO.setup(led,GPIO.OUT)

#GPIO.setwarnings(False)
def Main():
	#try:
		GPIO.output(led,GPIO.HIGH)
		time.sleep(2)
		while True:
			for x in range(1,6):
				GPIO.output(led,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(led,GPIO.LOW)
				time.sleep(0.5)
if __name__ == '__main__':
	Main()