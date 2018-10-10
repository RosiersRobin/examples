import struct
import time
from typing import Iterable

import serial

from settings import Settings

OP_START = 128
OP_STOP = 137
OP_CLEAN = 135
OP_SENSOR = 142
OP_QUERY_LIST = 149

PKT_BATTERY_CHARGE = 25
PKT_BATTERY_CAPACITY = 26

ser = serial.serial_for_url(Settings.ROOMBA_SERIAL, do_not_open=True)


def send_command(opcode: int, data_bytes=None):
    buffer = [opcode]
    if data_bytes:
        buffer += data_bytes
    ser.write(bytes(buffer))


def request_sensor(packet_id):
    send_command(OP_SENSOR, [packet_id])
    time.sleep(15e-3)       # wait 15ms for sensor data to be transmitted
    resp = ser.read_all()
    return resp


def request_list(*packet_ids: int):
    data_bytes = [len(packet_ids)] + packet_ids
    send_command(OP_QUERY_LIST, data_bytes)
    time.sleep(15e-3)       # wait 15ms for sensor data to be transmitted
    resp = ser.read_all()
    return resp


if __name__ == "__main__":
    try:
        ser.open()

        # command demo
        send_command(OP_START)
        time.sleep(1 / 2)
        send_command(OP_CLEAN)
        time.sleep(5)
        send_command(OP_STOP)
        time.sleep(1)

        # decode sensor data
        data = request_sensor(25)
        charge = struct.unpack(">H", data)
        print("Battery has {} mAh charge remaining.".format(charge))

        # multiple sensors
        data = request_list(25, 26)
        charge, capacity = struct.unpack(">HH", data)
        print("Battery has {:.1f}% charge remaining.".format(charge/capacity*100))

    finally:
        ser.close()
