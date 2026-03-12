import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected")
    exit()

j = pygame.joystick.Joystick(0)
j.init()

print("Controller:", j.get_name())
print("Axes:", j.get_numaxes())
print("Buttons:", j.get_numbuttons())
print("Hats:", j.get_numhats())
print("---------------------")

while True:

    pygame.event.pump()

    axes = [round(j.get_axis(i),2) for i in range(j.get_numaxes())]
    buttons = [j.get_button(i) for i in range(j.get_numbuttons())]
    hats = [j.get_hat(i) for i in range(j.get_numhats())]

    print("AXES :", axes)
    print("BUTTONS :", buttons)
    print("HATS :", hats)
    print("---------------------")

    time.sleep(0.5)