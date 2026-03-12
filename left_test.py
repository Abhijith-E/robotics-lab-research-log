import time
from motor_driver import MotorDriver

robot = MotorDriver()

def move_left(speed=20, duration=2):
    # Strafe LEFT
    robot.set_motor_speed(1, -speed)   # Front Left
    robot.set_motor_speed(2, speed)    # Front Right
    robot.set_motor_speed(3, speed)    # Rear Left
    robot.set_motor_speed(4, -speed)   # Rear Right

    time.sleep(duration)
    stop()

def stop():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)

try:
    move_left()
finally:
    stop()
