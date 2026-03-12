import pygame
import time
from motor_driver import MotorDriver

robot = MotorDriver()

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("USB PS2 Controller Connected!")

# ------------------------------
# SETTINGS
# ------------------------------
MAX_SPEED = 50
DEADZONE = 0.1

# ------------------------------
def stop():
    for m in range(1, 5):
        robot.set_motor_speed(m, 0)

def clamp(val):
    return int(max(-MAX_SPEED, min(MAX_SPEED, val)))

def apply_deadzone(value):
    if abs(value) < DEADZONE:
        return 0
    return value

# ------------------------------
try:
    while True:
        pygame.event.pump()

        # LEFT STICK
        lx = joystick.get_axis(0)   # left/right
        ly = joystick.get_axis(1)   # forward/back

        # RIGHT STICK
        rx = joystick.get_axis(2)   # rotation

        # Apply deadzone
        lx = apply_deadzone(lx)
        ly = apply_deadzone(ly)
        rx = apply_deadzone(rx)

        # Convert joystick values to speed
        forward = -ly * MAX_SPEED
        strafe  = -lx * MAX_SPEED   # FIXED: invert X axis
        rotate  = rx * MAX_SPEED

        # Mecanum drive calculation
        m1 = -(forward + strafe + rotate)
        m2 = -(forward - strafe - rotate)
        m3 = -(forward - strafe + rotate)
        m4 = -(forward + strafe - rotate)

        robot.set_motor_speed(1, clamp(m1))
        robot.set_motor_speed(2, clamp(m2))
        robot.set_motor_speed(3, clamp(m3))
        robot.set_motor_speed(4, clamp(m4))

        time.sleep(0.05)

except KeyboardInterrupt:
    stop()
    print("Stopped safely")

finally:
    stop()