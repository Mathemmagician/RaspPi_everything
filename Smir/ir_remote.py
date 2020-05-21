#!/usr/bin/env python

import time
import pigpio
import ir_hasher

counter = 0
def callback(hash):
    global counter
    print(f'{hash}: KEY_{counter}');
    counter += 1

print('one')
pi = pigpio.pi()
print('two')
ir = ir_hasher.hasher(pi, 17, callback, 5)
print('three')
print("ctrl c to exit");

time.sleep(30)

pi.stop()
