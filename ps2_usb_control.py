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

print("Controller Connected")

MAX_SPEED = 50
SLOW_SPEED = 25
DEADZONE = 0.1
speed_mode = MAX_SPEED


def stop():
    for m in range(1,5):
        robot.set_motor_speed(m,0)


def clamp(v):
    return int(max(-speed_mode, min(speed_mode, v)))


def apply_deadzone(v):
    if abs(v) < DEADZONE:
        return 0
    return v


try:

    while True:

        pygame.event.pump()

        # -----------------------
        # AXIS INPUT
        # -----------------------
        lx = apply_deadzone(joystick.get_axis(0))
        ly = apply_deadzone(joystick.get_axis(1))

        # Some controllers move rotation axis when mode changes
        rx = 0
        if joystick.get_numaxes() > 2:
            rx = apply_deadzone(joystick.get_axis(2))

        forward = -ly * speed_mode
        strafe  = -lx * speed_mode
        rotate  = rx * speed_mode

        # -----------------------
        # DPAD INPUT
        # -----------------------
        if joystick.get_numhats() > 0:
            hat = joystick.get_hat(0)

            if hat[1] == 1:
                forward = -speed_mode
            elif hat[1] == -1:
                forward = speed_mode

            if hat[0] == 1:
                strafe = speed_mode
            elif hat[0] == -1:
                strafe = -speed_mode

        # -----------------------
        # BUTTON INPUT
        # -----------------------
        buttons = joystick.get_numbuttons()

        A = joystick.get_button(0) if buttons > 0 else 0
        B = joystick.get_button(1) if buttons > 1 else 0
        X = joystick.get_button(2) if buttons > 2 else 0
        Y = joystick.get_button(3) if buttons > 3 else 0
        L1 = joystick.get_button(4) if buttons > 4 else 0
        R1 = joystick.get_button(5) if buttons > 5 else 0
        L2 = joystick.get_button(6) if buttons > 6 else 0
        R2 = joystick.get_button(7) if buttons > 7 else 0
        SELECT = joystick.get_button(8) if buttons > 8 else 0
        START = joystick.get_button(9) if buttons > 9 else 0
        MODE = joystick.get_button(10) if buttons > 10 else 0

        # -----------------------
        # SPECIAL BUTTONS
        # -----------------------

        if SELECT:   # emergency stop
            stop()
            continue

        if START:    # reset motion
            forward = 0
            strafe = 0
            rotate = 0

        if MODE:     # toggle speed
            if speed_mode == MAX_SPEED:
                speed_mode = SLOW_SPEED
            else:
                speed_mode = MAX_SPEED
            time.sleep(0.3)

        # rotation
        if B:
            rotate = speed_mode
        if X:
            rotate = -speed_mode

        # turbo forward
        if Y:
            forward = -speed_mode

        # diagonals
        if L1:
            forward = -speed_mode
            strafe = -speed_mode

        if R1:
            forward = -speed_mode
            strafe = speed_mode

        if L2:
            forward = speed_mode
            strafe = -speed_mode

        if R2:
            forward = speed_mode
            strafe = speed_mode

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