import sys

import machine

# ATTN_0DB ATTN_11DB ATTN_2_5DB ATTN_6DB
# WIDTH_9BIT WIDTH_10BIT WIDTH_11BIT WIDTH_12BIT

if sys.platform == 'LoPy4':
    adc = machine.ADC()  # create an ADC object

    def adc_read(pin: str):  # LoPy4
        ch = adc.channel(pin=pin, attn=machine.ADC.ATTN11DB)
        return ch.value()

    def adc_calibrate(pin='P22'):  # LoPy only?
        # Output Vref to pin
        adc.vref_to_pin(pin)

        vref = 0
        while not 900 < vref < 1300:
            print("Please measure the voltage on pin ", pin)
            val = input("Voltage (mV): ")
            vref = int(val)

        adc.vref(vref)


if sys.platform == 'esp32':

    def adc_read(pin: int):  # ESP32 (to be tested)
        pin = machine.Pin(pin)
        adc = machine.ADC(pin)  # create an ADC object
        adc.attn(machine.ADC.ATTN11DB)
        val = adc.read()  # read an analog value
        return val

