import RPi.GPIO as GPIO
import time
from interruptingcow import timeout
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

GPIO.setmode(GPIO.BOARD)

CS = 8
MISO = 9
MOSI = 10
CLK = 11

mcp = Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS, miso = MISO, mosi = MOSI)

led = 11
light_sensor = 0
sound_sensor = 1

#grovepi.pinMode(sound_sensor, "INPUT")

GPIO.setup(light_sensor, GPIO.IN)
GPIO.setup(sound_sensor, GPIO.IN)
GPIO.setup(led,GPIO.OUT)

sound_threshold = 400
light_threshold = 400

def Main():
	while True: #test suite
		for x in range(1,6):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.5)

		try:
			with timeout(5, exception=RuntimeError)
				while True:
					sound_value = grovepi.analogRead(light_sensor)
					time.sleep(0.1)
					resistance = (float)(1023 - sensor_value) * 10 / sensor_value

					if resistance > light_threshold:
						print("It is dark")
					else:
						print("It is light")
		except RuntimeError:
			pass

		for x in range(1,5):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.2)

		try:
			with timeout(5, exception=RuntimeError)
				while True:
					sensor_value = grovepi.analogRead(sound_sensor)
					time.sleep(0.1)
					if sensor_value > sound_threshold:
						GPIO.output(led,1)
						time.sleep(0.1)
						GPIO.output(led,0)
					else:
						GPIO.output(led,0)
		except RuntimeError:
			pass

		for x in range(1,5):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.2)

if __name__ == '__main__':
	Main()