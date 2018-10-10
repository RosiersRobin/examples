import serial
from serial.tools.miniterm import Miniterm

from settings import Settings

ser = serial.serial_for_url(Settings.LOPY_SERIAL, 115200)
xterm = Miniterm(ser, echo=False)
xterm.join()
