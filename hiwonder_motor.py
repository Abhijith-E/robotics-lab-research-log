import smbus
import time

class HiwonderMotor:
    def __init__(self, address=0x34):
        self.address = address
        self.bus = smbus.SMBus(1)

    def set_motor(self, motor_id, speed):
        """
        motor_id: 1 to 4
        speed: -100 to +100
        """
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100

        if speed < 0:
            direction = 1
            speed = abs(speed)
        else:
            direction = 0

        try:
            self.bus.write_i2c_block_data(self.address, motor_id, [direction, speed])
        except Exception as e:
            print("I2C Error:", e)

    def stop_all(self):
        for i in range(1, 5):
            self.set_motor(i, 0)
