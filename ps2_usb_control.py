import pygame
import time
from motor_driver import MotorDriver

robot = MotorDriver()

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Controller Connected")

MAX_SPEED = 50
BOOST_SPEED = 80
DEADZONE = 0.1


def stop():
    for m in range(1,5):
        robot.set_motor_speed(m,0)


def clamp(v):
    return int(max(-MAX_SPEED, min(MAX_SPEED, v)))


def apply_deadzone(v):
    if abs(v) < DEADZONE:
        return 0
    return v


try:

    while True:

        pygame.event.pump()

        forward = 0
        strafe = 0
        rotate = 0
        speed = MAX_SPEED

        # -----------------------
        # DPAD CONTROL
        # -----------------------

        if joystick.get_numhats() > 0:
            hat = joystick.get_hat(0)

            if hat == (0,1):      # UP
                forward = -speed

            elif hat == (0,-1):   # DOWN
                forward = speed

            elif hat == (-1,0):   # LEFT
                strafe = -speed

            elif hat == (1,0):    # RIGHT
                strafe = speed


        # -----------------------
        # BUTTONS
        # -----------------------

        A = joystick.get_button(0)
        B = joystick.get_button(1)
        X = joystick.get_button(2)
        Y = joystick.get_button(3)
        L1 = joystick.get_button(4)
        R1 = joystick.get_button(5)
        L2 = joystick.get_button(6)
        R2 = joystick.get_button(7)

        # BRAKE
        if A:
            stop()
            time.sleep(0.05)
            continue

        # SPEED BOOST
        if Y:
            speed = BOOST_SPEED

        # ROTATION
        if X:
            rotate = -speed

        if B:
            rotate = speed

        # DIAGONALS
        if L1:
            forward = -speed
            strafe = -speed

        if L2:
            forward = speed
            strafe = -speed

        if R1:
            forward = -speed
            strafe = speed

        if R2:
            forward = speed
            strafe = speed


        # -----------------------
        # MECANUM CALCULATION
        # -----------------------

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