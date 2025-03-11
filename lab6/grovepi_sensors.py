# Tina Habibi
# Faith Klein

import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# LCD connected to port 
# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    threshold = grovepi.analogRead(potentiometer)
    
    # TODO: format LCD text according to threshhold
    top_line = f"{threshold} cm"
    
    if distance < threshold:
      top_line += "OBJ PRES"

    bottom_line = f"{distance} cm"

    # Display text on LCD
    setText_norefresh(f"{top_line}\n{bottom_line}")

    time.sleep(0.5)  # Add delay to avoid excessive updates
    
  except IOError:
    print("Error")