# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from gyroscope import Gyroscope


pixel_pin = board.D18 # NeoPixels must be connected to D10, D12, D18 or D21 to work.
num_pixels = 100 # Num of neopixels. 240 is my max
ORDER = neopixel.GRB # My strip needs this line for normal RGB format

g = Gyroscope()

with neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER) as pixels:
    while True:
        x, y, z = g.get_xyz_acceleration()
        pixels.fill((0, 0, 0))
        if abs(x) > 0.3:
            if x > 0:
                print('right')
                c = 0
            else:
                print('left')
                c = 1
            pixels[c::2] = [(100, 0, 0)] * (len(pixels) // 2)
        else:
            pixels.fill((0, 100, 0))

        #pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(0.2)

