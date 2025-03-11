# Tina Habibi
# Faith Klein

import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold = 500  # change this value
sound_treshold = 600 # change this value

pin = 11 # ??
light_sensor_channel = 0
sound_sensor_channel = 1

while True: 
  time.sleep(0.5) 

  # 1. Blink the LED 5 times with on/off intervals of 500ms.
  for _ in range(5):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)

  # 2. Read and print light signal for 5 seconds
  start_time = time.time()
  while time.time() - start_time < 5:
    # get reading from adc 
    adc = mcp.read_adc(light_sensor_channel) 
    print(adc, " bright" if adc > lux_treshold else " dark")
    time.sleep(0.1)
  
  # 3. Blink the LED 4 times with on/off intervals of 200ms
  for _ in range(4):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)

  # 4. Read and print sound signal, blink LED if mic tapped
  start_time = time.time()
  while time.time() - start_time < 5:
    adc = mcp.read_adc(sound_sensor_channel) 
    print(adc)
    if adc > sound_treshold:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)
    
    time.sleep(0.1)  

