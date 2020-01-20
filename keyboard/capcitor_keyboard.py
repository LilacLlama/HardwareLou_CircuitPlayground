# Demo keyboard module
# Turn the switch on to begin

import time

from adafruit_circuitplayground import cpb

THRESHOLD = 100
cp.adjust_touch_threshold(THRESHOLD)

# Super loop
while True:
    if cpb.switch:
        cpb.pixels[:] = (0, 0, 0)
        if cpb.touch_A0 > THRESHOLD:
            cpb.pixels[5] = (255, 0, 0)
            cpb.pixels[6] = (255, 0, 0)
            cpb.play_tone(352, 100)
        elif cpb.touch_A1 > THRESHOLD:
            cpb.pixels[6] = (200, 128, 0)
            cpb.pixels[7] = (200, 128, 0)
            cpb.play_tone(395, 1)
        if cpb.touch_A2 > THRESHOLD:
            cpb.pixels[7] = (100, 180, 0)
            cpb.pixels[8] = (100, 180, 0)
            cpb.play_tone(418, 1)
        if cpb.touch_A3 > THRESHOLD:
            cpb.pixels[8] = (0, 255, 0)
            cpb.pixels[9] = (0, 255, 0)
            cpb.play_tone(469, 1)
        if cpb.touch_A4 > THRESHOLD:
            cpb.pixels[0] = (0, 180, 128)
            cpb.pixels[1] = (0, 180, 128)
            cpb.play_tone(527, 1)
        if cpb.touch_A5 > THRESHOLD:
            cpb.pixels[1] = (0, 60, 200)
            cpb.pixels[2] = (0, 60, 200)
            cpb.play_tone(558, 1)
        if cpb.touch_A6 > THRESHOLD:
            cpb.pixels[2] = (0, 0, 255)
            cpb.pixels[3] = (0, 0, 255)
            cpb.play_tone(627, 1)
        if cpb.touch_A7 > THRESHOLD:
            cpb.pixels[3] = (150, 0, 180)
            cpb.pixels[4] = (150, 0, 180)
            cpb.play_tone(704, 1)
    else:
        cpb.pixels[:] = (0, 0, 0)
