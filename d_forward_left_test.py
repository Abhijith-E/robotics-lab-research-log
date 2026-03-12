import time
from motor_driver import MotorDriver

robot = MotorDriver()

def move_back_diagonal_right(speed=20, duration=2):
    robot.set_motor_speed(1, -speed)
    robot.set_motor_speed(2, 0)
    robot.set_motor_speed(3, 0)
    robot.set_motor_speed(4, -speed)

    time.sleep(duration)
    stop()

def stop():
    for m in range(1,5):
        robot.set_motor_speed(m,0)

try:
    move_back_diagonal_right()
finally:
    stop()