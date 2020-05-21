import socket
import pickle
from time import sleep

from gyroscope import Gyroscope

import board
import neopixel


# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
num_pixels = 143
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


g = Gyroscope()
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.240', 1235))
s.listen(1)


shift = 0
ftime = 0
def turning(w):
    # w is width 
    global pixels, shift
    for i in range(w):
        for j in range((shift+i)%(2*w), num_pixels, 2*w):
            pixels[j] = (0, 0, 100) 
    for i in range(w, 2*w):
        for j in range((shift+i)%(2*w), num_pixels, 2*w):
            pixels[j] = (255,69,0)

def forward(w):
    global pixels, ftime
    pixels.fill((0, 0, 0))
    for i in range(w):
        pixels[(60+ftime+i)%num_pixels] = (0, 100, 0)
        pixels[(59-ftime-i)%num_pixels] = (0, 100, 0)


yhist = [0, 0, 0, 0, 0]

while True:
    #clientsocket, address = s.accept()
    #print(f'Connection from {address} has been established!')
    
    while True:
        data = g.get_xyz_rotation_radians()
        yhist = yhist[1:] + [data['y']]
        avey = sum(yhist) / len(yhist)
        if avey > 0.15:
            #pixels.fill((100, 0, 0))
            turning(4)
            shift += 1
        elif avey < -0.05:
            pixels.fill((0, 0, 100))
            turning(4)
            shift -= 1
        else:
            forward(10)
            ftime += 2
            #pixels.fill((0, 100, 0))
        pixels.show()
        #msg = pickle.dumps(data)

        #msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
        #clientsocket.send(msg)
        #print('Message sent')
        #sleep(0.5)


