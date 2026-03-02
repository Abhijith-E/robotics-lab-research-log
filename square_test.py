import time
from motor_driver import MotorDriver

robot = MotorDriver()

# =============================
# TUNING PARAMETERS
# =============================
FORWARD_SPEED = 25
TURN_SPEED = 25

FORWARD_TIME = 2.8      # Adjust to get exact 1 meter
TURN_TIME = 0.75        # Adjust to get exact 90 degrees

BRAKE_DELAY = 0.2

# =============================
# BASIC MOTOR CONTROL
# =============================

def stop():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)
    time.sleep(BRAKE_DELAY)


# =============================
# FORWARD MOVEMENT
# =============================

def forward():
    # All motors same direction
    robot.set_motor_speed(1, -FORWARD_SPEED)
    robot.set_motor_speed(2, -FORWARD_SPEED)
    robot.set_motor_speed(3, -FORWARD_SPEED)
    robot.set_motor_speed(4, -FORWARD_SPEED)

    time.sleep(FORWARD_TIME)
    stop()


# =============================
# ROTATE RIGHT (90 DEG)
# =============================

def rotate_right():
    # Left wheels backward
    robot.set_motor_speed(1, -TURN_SPEED)
    robot.set_motor_speed(3, -TURN_SPEED)

    # Right wheels forward
    robot.set_motor_speed(2, TURN_SPEED)
    robot.set_motor_speed(4, TURN_SPEED)

    time.sleep(TURN_TIME)
    stop()


# =============================
# MAIN SQUARE LOOP
# =============================

try:
    print("Starting square movement...")

    for i in range(4):
        print(f"Side {i+1}")
        forward()
        rotate_right()

    print("Square completed!")

finally:
    stop()
