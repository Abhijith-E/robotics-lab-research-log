import time
from motor_driver import MotorDriver

robot = MotorDriver()

def move_back_diagonal_left(speed=20, duration=2):
    robot.set_motor_speed(1, 0)
    robot.set_motor_speed(2, -speed)
    robot.set_motor_speed(3, -speed)
    robot.set_motor_speed(4, 0)

    time.sleep(duration)
    stop()

def stop():
    for m in range(1,5):
        robot.set_motor_speed(m,0)

try:
    move_back_diagonal_left()
finally:
    stop()