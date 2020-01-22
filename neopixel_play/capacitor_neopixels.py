# Demo module for testing board
# Flip the switch to turn on/off the buzzer

import time

from adafruit_circuitplayground import cp

red = 0
green = 0
blue = 0
pixels = 10

COLOR_MAX = 255

print("Circuit Playground Test!")

# Super loop
while True:
    if cp.switch:
        if cp.touch_A1:
            pixels += 1
        if cp.touch_A2:
            red += 25
        if cp.touch_A3:
            red -= 25
        if cp.touch_A4:
            blue += 25
        if cp.touch_A5:
            blue -= 25
        if cp.touch_A6:
            green += 25
        if cp.touch_A7:
            green -= 25

        # Clear all pixels before fill
        cp.pixels.fill((0, 0, 0))

        # No more than 10 NeoPixel indices (0 indexed) prevent overflow
        pixels = 1 if pixels > 10 else pixels

        # Reset color if overflow
        red = 0 if red > COLOR_MAX else red
        blue = 0 if blue > COLOR_MAX else blue
        green = 0 if green > COLOR_MAX else green

        print(pixels, red, green, blue)

        for i in range(pixels):
            cp.pixels[i] = (red, green, blue)
    else:
        # Slide is off clear all pixels
        cp.pixels.fill((0, 0, 0))
    time.sleep(1)
