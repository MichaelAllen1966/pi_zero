import time
from machine import Pin

onboardLED = Pin(25, Pin.OUT)
for i in range(10):
    if onboardLED.value() == 0:
        onboardLED.value(1)
    else:
        onboardLED.value(0)
    time.sleep(0.25)
