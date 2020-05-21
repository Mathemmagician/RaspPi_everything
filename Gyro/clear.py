import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 240)

for i in range(240):
	pixels[i] = (0, 0, 0)
