import time

import serial
ser = serial.serial_for_url("/dev/ttyUSB0", 115200)

try:
    ser.open()
    while True:
        line = input("serial>")
        ser.write(bytes([int(x, 0) for x in line.replace(",", " ").split()]))
        time.sleep(20e-3)
        if ser.in_waiting:
            rsp = ser.read_all()
            print(rsp)

except KeyboardInterrupt:
    print("Bye.")
finally:
    ser.close()
