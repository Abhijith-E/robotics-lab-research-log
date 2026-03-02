import smbus

I2C_ADDR = 0x34  # fixed I2C address

class MotorDriver:
    def __init__(self, bus_num=1):
        self.bus = smbus.SMBus(bus_num)

    def set_motor_speed(self, motor_id, speed):
        # Normalize speed from -100..100
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100

        # Clamp motor id 1–4
        if not (1 <= motor_id <= 4):
            raise ValueError("Invalid motor id")

        register = 50 + motor_id
        # speed is a signed byte
        self.bus.write_i2c_block_data(I2C_ADDR, register, [speed])

    def set_all(self, speed):
        # speed to all motors using register 51
        self.bus.write_i2c_block_data(I2C_ADDR, 51, [speed])

    def stop(self):
        # set all motors speed to 0
        self.set_all(0)
