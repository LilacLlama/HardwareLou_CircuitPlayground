# Demo module for testing library and board
# flip the switch to turn on/off the snap sensor

import time

from adafruit_circuitplayground import cpb

snapped = false
color_shift = 0
color_max = 7
cp.pixels.brightness = 0.3

print("Circuit Playground snap sensor!")

rainbow_grid = {
    0: (255,   0,   0),
    1: (180,   60,   0),
    2: (60,   180,   0),
    3: (0,   255,   0),
    4: (0,   180,   60),
    5: (0,   60,   180),
    6: (0,   0,   255),
    7: (60,   0,   180),
    8: (180,   0,   60),
    9: (255,   0,   0),
}

def paint_pixels(pattern_index):
    """
    Take an index value from 0 to 6 and create
    a color pattern with the neopixels.
    """
    if pattern_index = 0: # RAINBOW
        for i in range(10):
            cpb.pixels[i] = rainbow_grid[i]
    elif pattern_index = 1: # RED!
        cpb.pixels[0:9] = (255, 0, 0)
    elif pattern_index = 2: # BLUE!
        cpb.pixels[0:9] = (0, 255, 0)
    elif pattern_index = 3: # GREEN!
        cpb.pixels[0:9] = (0, 0, 255)
    elif pattern_index = 4: # YELLOW & TEAL!
        cpb.pixels[0:8:2] = (255, 150, 0)
        cpb.pixels[1:9:2] = (0, 255, 255)
    elif pattern_index = 5: # PURPLE & MAGENTA!
        cpb.pixels[0:8:2] = (180, 0, 255)
        cpb.pixels[1:9:2] = (255, 0, 255)
    elif pattern_index = 6: # GREEN & ORANGE!
        cpb.pixels[0:8:2] = (0, 255, 0)
        cpb.pixels[1:9:2] = (255, 165, 0)
    else: # OH DEAR
        cp.pixels.brightness = 1.0
        cpb.pixels[0:9] = (255, 255, 255)


# Super loop
while True:
    if cpb.switch:
        if cpb.sound_level > 1000 and not snapped:
            print("SNAP ON!")
            snapped = True
            # 0 to 6
            if color_shift < color_max:
                paint_pixels(color_shift)
                color_shift+=1
                # Reset on 7 to always stay below max
                if color_shift = color_max:
                    color_shift = 0
        elif cpb.sound_level > 1000 and snapped:
            snapped = False
            print("SNAP OFF!")
            cpb.pixels[:] = (0, 0, 0)
    else:
        cpb.pixels[:] = (0, 0, 0)
    time.sleep(2.5)
