import pygame
import time
import os

# Disable audio warnings (ALSA fix)
os.environ["SDL_AUDIODRIVER"] = "dummy"

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("\n=== JOYSTICK INFORMATION ===")
print("Name:", joystick.get_name())
print("Number of Axes:", joystick.get_numaxes())
print("Number of Buttons:", joystick.get_numbuttons())
print("Number of Hats:", joystick.get_numhats())
print("============================\n")

try:
    while True:
        pygame.event.pump()

        print("----- AXES -----")
        for i in range(joystick.get_numaxes()):
            value = joystick.get_axis(i)
            print(f"Axis {i}: {round(value, 3)}")

        print("----- BUTTONS -----")
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                print(f"Button {i}: PRESSED")

        print("----- HATS (D-PAD) -----")
        for i in range(joystick.get_numhats()):
            hat = joystick.get_hat(i)
            print(f"Hat {i}: {hat}")

        print("\n============================\n")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting safely...")
