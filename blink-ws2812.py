# Change colors on the built-in WS2812 RGB LED on the C5 Dev Module
# Standard blink toggling pin 27 will not  work for this RGB LED

# basic_ws2112.py - Basic WS2112 control
import machine
import neopixel
import time

# Configure WS2112 LED
# neopixel.NeoPixel(pin, number_of_leds, bpp=3, timing=1)
np = neopixel.NeoPixel(machine.Pin(27), 1)

def set_color(r, g, b):
    """Set LED to specific RGB color"""
    np[0] = (r, g, b)
    np.write()

def test_colors():
    """Test basic colors"""
    colors = [
        (1, 0, 0),    # Red
        (0, 1, 0),    # Green
        (0, 0, 1),    # Blue
        (1, 1, 0),  # Yellow
        (1, 0, 1),  # Magenta
        (0, 1, 1),  # Cyan
        (1, 1, 1) # White
    ]
    
    print("Testing basic colors...")
    for i, color in enumerate(colors):
        set_color(*color)
        print(f"Color {i+1}: RGB{color}")
        time.sleep(1)
    
    # Turn off LED
    set_color(0, 0, 0)
    print("Color test complete!")

# Run test
test_colors()