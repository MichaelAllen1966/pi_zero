# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


red.value(0)

while True: # Loop forever
    
    time.sleep(0.2) # Short Delay
    
    if button1.value() == 1:
        green.value(1) # green LED on
        red.value(0) # red LED off
        amber.value(0) # amber LED off
        
    elif button2.value() == 1:
        green.value(0) # green LED off
        red.value(0) # red LED off
        amber.value(1) # amber LED on
        
    elif button3.value() == 1:
        green.value(0) # green LED off
        red.value(1) # red LED on
        amber.value(0) # amber LED off
        
    elif button1.value == 1 and button2.value == 1 and button3.value == 1:
        green.value(0) # green LED off
        red.value(0) # red LED off
        amber.value(0) # amber LED off