# Demo module for testing library and board
# flip the switch to turn on/off the snap sensor

import array
import math
import time

import audiobusio
import board
from adafruit_circuitplayground import cp

snapped = False
color_shift = 0
color_max = 7
cp.pixels.brightness = 0.3

print("Circuit Playground snap sensor!")

def mean(values):
    return sum(values) / len(values)

def normalized_rms(values):
    minbuf = int(mean(values))
    sum_of_samples = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )
    return math.sqrt(sum_of_samples / len(values))

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
    if pattern_index == 0: # RAINBOW
        for i in range(10):
            cp.pixels[i] = rainbow_grid[i]
    elif pattern_index == 1: # RED!
        cp.pixels.fill((255, 0, 0))
    elif pattern_index == 2: # BLUE!
        cp.pixels.fill((0, 255, 0))
    elif pattern_index == 3: # GREEN!
        cp.pixels.fill((0, 0, 255))
    elif pattern_index == 4: # YELLOW & TEAL!
        for i in range(0, 10, 2):
            print(i)
            cp.pixels[i] = (255, 150, 0)
        for i in range(1, 11, 2):
            print(i)
            cp.pixels[i] = (0, 255, 255)
    elif pattern_index == 5: # PURPLE & MAGENTA!
        for i in range(0, 10, 2):
            print(i)
            cp.pixels[i] = (180, 0, 255)
        for i in range(1, 11, 2):
            print(i)
            cp.pixels[i] = (255, 0, 255)
    elif pattern_index == 6: # GREEN & ORANGE!
        for i in range(0, 10, 2):
            print(i)
            cp.pixels[i] = (0, 255, 0)
        for i in range(1, 11, 2):
            print(i)
            cp.pixels[i] = (255, 165, 0)
    else: # OH DEAR
        cp.pixels.brightness = 1.0
        cp.pixels.fill((255, 255, 255))


mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)
samples = array.array('H', [0] * 160)
mic.record(samples, len(samples))

# Super loop
while True:
    if cp.switch:
        mic.record(samples, len(samples))
        magnitude = normalized_rms(samples)
        print(((magnitude),))
        if magnitude > 90 and not snapped:
            print("SNAP ON!")
            snapped = True
            # 0 to 6
            if color_shift < color_max:
                paint_pixels(color_shift)
                color_shift+=1
                # Reset on 7 to always stay below max
                if color_shift == color_max:
                    color_shift = 0
        elif magnitude > 90 and snapped:
            snapped = False
            print("SNAP OFF!")
            cp.pixels.fill(0)
    else:
        cp.pixels.fill(0)
    time.sleep(1.5)
