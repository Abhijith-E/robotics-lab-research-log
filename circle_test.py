import time
from motor_driver import MotorDriver

robot = MotorDriver()

def move_circle(speed=100, turn_speed=10, duration=6):
    """
    speed = forward speed
    turn_speed = how tight the circle is
    duration = how long to move
    """

    print("Moving in a circle...")

    # Forward + slight right rotation combined
    robot.set_motor_speed(1, -(speed + turn_speed))  # Front Left
    robot.set_motor_speed(2, -(speed - turn_speed))  # Front Right
    robot.set_motor_speed(3, -(speed + turn_speed))  # Rear Left
    robot.set_motor_speed(4, -(speed - turn_speed))  # Rear Right

    time.sleep(duration)
    stop()

def stop():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)
    time.sleep(0.3)

try:
    move_circle(speed=20, turn_speed=10, duration=6)

finally:
    stop()
    print("Circle movement complete.")
