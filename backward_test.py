import time
from motor_driver import MotorDriver

robot = MotorDriver()

def backward(speed=20, duration=3.5):
    robot.set_motor_speed(1, speed)
    robot.set_motor_speed(2, speed)
    robot.set_motor_speed(3, speed)
    robot.set_motor_speed(4, speed)

    time.sleep(duration)
    stop()

def stop():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)

try:
    backward()
finally:
    stop()
