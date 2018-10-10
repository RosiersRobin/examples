import machine

adc = machine.ADC()  # create an ADC object

# ATTN_0DB ATTN_11DB ATTN_2_5DB ATTN_6DB
# WIDTH_9BIT WIDTH_10BIT WIDTH_11BIT WIDTH_12BIT


adc.atten(machine.ADC.ATTN_11DB)


def adc_read(pin):
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
