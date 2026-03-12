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

MAX_SPEED = 50
DEADZONE = 0.1


def stop():
    for m in range(1,5):
        robot.set_motor_speed(m,0)


def clamp(val):
    return int(max(-MAX_SPEED, min(MAX_SPEED, val)))


def apply_deadzone(v):
    if abs(v) < DEADZONE:
        return 0
    return v


try:
    while True:

        pygame.event.pump()

        # ----------------------
        # AXIS CONTROL (JOYSTICK)
        # ----------------------
        lx = apply_deadzone(joystick.get_axis(0))
        ly = apply_deadzone(joystick.get_axis(1))
        rx = apply_deadzone(joystick.get_axis(2))

        forward = -ly * MAX_SPEED
        strafe = -lx * MAX_SPEED
        rotate = rx * MAX_SPEED

        # ----------------------
        # DPAD CONTROL
        # ----------------------
        hat = joystick.get_hat(0)

        if hat[1] == 1:      # UP
            forward = -MAX_SPEED
        elif hat[1] == -1:   # DOWN
            forward = MAX_SPEED

        if hat[0] == 1:      # RIGHT
            strafe = MAX_SPEED
        elif hat[0] == -1:   # LEFT
            strafe = -MAX_SPEED

        # ----------------------
        # BUTTON CONTROL
        # ----------------------

        A = joystick.get_button(0)
        B = joystick.get_button(1)
        X = joystick.get_button(2)
        Y = joystick.get_button(3)
        L1 = joystick.get_button(4)
        R1 = joystick.get_button(5)
        L2 = joystick.get_button(6)
        R2 = joystick.get_button(7)

        # STOP
        if A:
            stop()
            continue

        # ROTATE
        if B:
            rotate = MAX_SPEED
        if X:
            rotate = -MAX_SPEED

        # TURBO FORWARD
        if Y:
            forward = -MAX_SPEED

        # DIAGONALS
        if L1:
            forward = -MAX_SPEED
            strafe = -MAX_SPEED

        if R1:
            forward = -MAX_SPEED
            strafe = MAX_SPEED

        if L2:
            forward = MAX_SPEED
            strafe = -MAX_SPEED

        if R2:
            forward = MAX_SPEED
            strafe = MAX_SPEED

        # ----------------------
        # MECANUM CALCULATION
        # ----------------------

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