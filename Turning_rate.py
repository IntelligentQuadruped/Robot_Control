from robot import Robot
import time
from math import degrees

robot = Robot()
robot.connect('/dev/tty.usbserial-DN01QALN',115200)


print(">>> Start test sequence")

start = time.time()
dt = 0
received = False

while received:
    if robot.command() != None:
        received = robot.command()
    

print("starting for loop")

try:
    dt = 0
    start  = time.time()
    print("Should turn with %.3f degrees/sec"%(degrees((0.3*0.2))))
    while dt<10 :
        dt = time.time() - start
        robot.command(forward = 0.3, turn = 0.2)
    while(True):
        robot.command()
    
except KeyboardInterrupt:
    print(">>> Test sequence interupted")

  

robot.disconnect()
print("Robot disconnected. Test complete")






    