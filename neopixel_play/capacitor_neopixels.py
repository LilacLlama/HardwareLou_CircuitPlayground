# Demo module for testing board
# Flip the switch to turn on/off the buzzer

import time

from adafruit_circuitplayground import cpb

red = 100
green = 50
blue = 25
pixels = 9

THRESHOLD = 100

print("Circuit Playground Test!")

cp.adjust_touch_threshold(THRESHOLD)

# Super loop
while True:
    if cpb.switch:
        if cpb.touch_A0 > THRESHOLD:
            pixels += 1
        elif cpb.touch_A1 > THRESHOLD:
            pixels -= 1
        if cpb.touch_A2 > THRESHOLD:
            red += 25
        if cpb.touch_A3 > THRESHOLD:
            red -= 25
        if cpb.touch_A4 > THRESHOLD:
            blue += 25
        if cpb.touch_A5 > THRESHOLD:
            blue -= 25
        if cpb.touch_A6 > THRESHOLD:
            green += 25
        if cpb.touch_A7 > THRESHOLD:
            green -= 25

        # Clear all pixels before fill
        cpb.pixels[:] = (0, 0, 0)

        # No more than 10 NeoPixel indices (0 indexed)
        pixels = 9 if pixels > 9 else pixels

        for i in range(pixels):
            cpb.pixels[i] = (RED, GREEN, BLUE)
    else:
        # Slide is off clear all pixels
        cpb.pixels[:] = (0, 0, 0)
    time.sleep(2.5)
