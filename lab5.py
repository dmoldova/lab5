import RPi.GPIO as GPIO
import time
#from interruptingcow import timeout
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

GPIO.setmode(GPIO.BCM)

CS = 8
MISO = 9
MOSI = 10
CLK = 11

mcp = Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS, miso = MISO, mosi = MOSI)

#SPI_PORT = 0
#SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

led = 17
light_sensor = 0
sound_sensor = 1

#grovepi.pinMode(sound_sensor, "INPUT")

GPIO.setup(light_sensor, GPIO.IN)
GPIO.setup(sound_sensor, GPIO.IN)
GPIO.setup(led,GPIO.OUT)

sound_threshold = 500
light_threshold = 500

def Main():
	while True: #test suite
		for x in range(1,6):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.5)

		for x in range(0, 50):
			light_value = mcp.read_adc(light_sensor)
			#print(light_value)
			if (light_value > light_threshold):
				print(str(light_value) + " Bright")
			else:
				print(str(light_value) + " Dark")
			time.sleep(0.1)

		for x in range(1,5):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.2)

		for x in range(0, 50):
			sound_value = mcp.read_adc(sound_sensor)
			print(sound_value)
			if (sound_value > sound_threshold):
				GPIO.output(led, GPIO.HIGH)
				time.sleep(0.1)
				GPIO.output(led, GPIO.LOW)
			else:
				time.sleep(0.1)

		for x in range(1,5):
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(led,GPIO.LOW)
			time.sleep(0.2)

if __name__ == '__main__':
	Main()