# Works only if your module uses a standard single color LED
# If you have a multi-color LED, you must use the blink-ws2812.py script

from machine import Pin
import time

# Define GPIO27
led = Pin(27, Pin.OUT)

while True:
    # Low-level illumination
    led.value(0)
    print("LED ON")
    time.sleep(1) # Wait for 1 second
    
    # High-level extinction
    led.value(1)
    print("LED OFF")
    time.sleep(1)
    print("bla")