import time

import network

ESSID = "NMCT-rPI"
WPA_PSK = "88VNncvQGy"


def do_connect(essid, wpa_psk):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, wpa_psk)
        while not wlan.isconnected():
            time.sleep(1/10)
    print('network config:', wlan.ifconfig())


if __name__ == "__main__":
    do_connect(ESSID, WPA_PSK)
