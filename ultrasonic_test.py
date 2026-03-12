import smbus
import time

bus = smbus.SMBus(1)
address = 0x77

while True:
    try:
        # Read 2 bytes from register 0x00
        data = bus.read_i2c_block_data(address, 0x00, 2)

        # Swap bytes (little endian fix)
        distance = data[1] << 8 | data[0]

        # Filter invalid values
        if distance > 5000:
            print("Out of range")
        else:
            print("Distance:", distance, "mm")

        time.sleep(0.5)

    except Exception as e:
        print("Error:", e)
        time.sleep(1)
