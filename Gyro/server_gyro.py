'''In this file we simply read the gyro info 
and upload it to the apachi server test.txt file
which can be the parsed on a local machine
'''
from math import sin, cos, radians
from time import sleep, time

from gyroscope import Gyroscope

def uploadGyroXYZ():
    x, y, z = g.get_xyz_rotation()
    filename = "/var/www/html/test.txt" 
    with open(filename, "w") as f:
        f.write(f"{x},{y},{z}")

g = Gyroscope()

if __name__ == '__main__':

    ptime = time()

    for i in range(5):
        uploadGyroXYZ()
        ctime = time()
        print(f'i = {i} {ctime - ptime}')
        ptime = ctime
        sleep(1)
