import sys

import machine

adc = machine.ADC()  # create an ADC object


# ATTN_0DB ATTN_11DB ATTN_2_5DB ATTN_6DB
# WIDTH_9BIT WIDTH_10BIT WIDTH_11BIT WIDTH_12BIT

def adc_attn(pin: str):  # LoPy4
    ch = adc.channel(pin=pin, attn=machine.ADC.ATTN11DB)
    return ch.value()


def adc_read(pin: int):  # ESP32 (to be tested)
    pin = machine.Pin(pin)
    ch = adc.channel(pin=pin)  # create an analog pin on GP3
    val = ch.value()  # read an analog value
    return val


def adc_calibrate(pin='P22'):  # LoPy only?
    # Output Vref to pin
    adc.vref_to_pin(pin)

    vref = 0
    while not 900 < vref < 1300:
        print("Please measure the voltage on pin ", pin)
        val = input("Voltage (mV): ")
        vref = int(val)

    adc.vref(vref)


if __name__ == "__main__":
    if sys.platform == "LoPy4":
        adc_calibrate()
