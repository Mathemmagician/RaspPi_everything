#!/usr/bin/env python

import time
import pigpio
import ir_hasher
import json

def callback(hash):
    global key, data, recorded
    data[key] = hash
    print(f"hash={hash} recorded as {key}");
    recorded = 1


print('Welcome to Ramils Remote Setuper')
print('This code creates a json dictionary mapping keynames to their IR hashcodes')
print('Make sure you have pigpio installed, pigpiod enabled and have ir_hasher ')

print('='*30, '\n', 'The default pin for IR receiver is 17')
print('Setting up PI gpios and hasher')

INPUT_PIN = 17
pi = pigpio.pi()
ir = ir_hasher.hasher(pi, INPUT_PIN, callback, 5)

print("Type key name, press ENTER, then press key on remote. Repeat. Succeed.")
print("Empty input to stop")

data = {}
key = input("Type key name: ")
recorded = 0

while key != "":
    print("Press that key")
    while recorded == 0:
        pass
    print('recorded')
    recorded = 0 
    key = input("Type next key name: ")

pi.stop()
with open('remote.txt', 'w') as outfile:
    json.dump(data, outfile)
