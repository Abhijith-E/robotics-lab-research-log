import time
from motor_driver import MotorDriver

robot = MotorDriver()

def forward(speed=60):
    for m in range(1, 5):
        robot.set_motor_speed(m, speed)

def backward(speed=60):
    for m in range(1, 5):
        robot.set_motor_speed(m, -speed)

def left(speed=60):
    robot.set_motor_speed(1, -speed)
    robot.set_motor_speed(2, speed)
    robot.set_motor_speed(3, speed)
    robot.set_motor_speed(4, -speed)

def right(speed=60):
    robot.set_motor_speed(1, speed)
    robot.set_motor_speed(2, -speed)
    robot.set_motor_speed(3, -speed)
    robot.set_motor_speed(4, speed)

def rotate_left(speed=60):
    robot.set_motor_speed(1, -speed)
    robot.set_motor_speed(2, speed)
    robot.set_motor_speed(3, -speed)
    robot.set_motor_speed(4, speed)

def rotate_right(speed=60):
    robot.set_motor_speed(1, speed)
    robot.set_motor_speed(2, -speed)
    robot.set_motor_speed(3, speed)
    robot.set_motor_speed(4, -speed)

def stop_all():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)
    time.sleep(0.2)

try:
    print("Forward")
    forward()
    time.sleep(2)
    stop_all()

    print("Backward")
    backward()
    time.sleep(2)
    stop_all()

    print("Left")
    left()
    time.sleep(2)
    stop_all()

    print("Right")
    right()
    time.sleep(2)
    stop_all()

    print("Rotate Left")
    rotate_left()
    time.sleep(2)
    stop_all()

    print("Rotate Right")
    rotate_right()
    time.sleep(2)
    stop_all()

finally:
    # VERY IMPORTANT: always stop motors when program exits
    stop_all()
    print("All motors stopped safely.")
