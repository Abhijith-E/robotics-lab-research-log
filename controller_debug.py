import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Controller Name:", joystick.get_name())
print("Axes:", joystick.get_numaxes())
print("Buttons:", joystick.get_numbuttons())
print("Hats:", joystick.get_numhats())
print("Move sticks and press buttons to see values\n")

while True:

    pygame.event.pump()

    # AXES
    for i in range(joystick.get_numaxes()):
        val = joystick.get_axis(i)
        if abs(val) > 0.1:
            print("Axis", i, "=", round(val, 2))

    # BUTTONS
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            print("Button pressed:", i)

    # DPAD
    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        if hat != (0,0):
            print("DPad:", hat)

    time.sleep(0.1)