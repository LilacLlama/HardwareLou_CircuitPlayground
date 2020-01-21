# Demo keyboard module
# Turn the switch on to begin

import time

from adafruit_circuitplayground import cp

# Super loop
while True:
    if cp.switch:
        cp.pixels.fill((0, 0, 0))
        if cp.touch_A1:
            cp.pixels[5] = (255, 0, 0)
            cp.pixels[6] = (200, 128, 0)
            cp.play_tone(395, 1)
        if cp.touch_A2:
            cp.pixels[7] = (100, 180, 0)
            cp.pixels[8] = (100, 180, 0)
            cp.play_tone(418, 1)
        if cp.touch_A3:
            cp.pixels[8] = (0, 255, 0)
            cp.pixels[9] = (0, 255, 0)
            cp.play_tone(469, 1)
        if cp.touch_A4:
            cp.pixels[0] = (0, 180, 128)
            cp.pixels[1] = (0, 180, 128)
            cp.play_tone(527, 1)
        if cp.touch_A5:
            cp.pixels[1] = (0, 60, 200)
            cp.pixels[2] = (0, 60, 200)
            cp.play_tone(558, 1)
        if cp.touch_A6:
            cp.pixels[2] = (0, 0, 255)
            cp.pixels[3] = (0, 0, 255)
            cp.play_tone(627, 1)
        if cp.touch_A7:
            cp.pixels[3] = (150, 0, 180)
            cp.pixels[4] = (150, 0, 180)
            cp.play_tone(704, 1)
    else:
        cp.pixels.fill((0, 0, 0))
