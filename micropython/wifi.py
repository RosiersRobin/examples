import time

import network

ESSID = "NMCT-rPI"
WPA_PSK = "88VNncvQGy"


def do_connect(essid, wpa_psk):
    wlan = network.WLAN(mode=network.WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == essid:
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, wpa_psk), timeout=5000)
            while not wlan.isconnected():
                machine.idle()  # save power while waiting
            print('WLAN connection succeeded!')
            break


if __name__ == "__main__":
    do_connect(ESSID, WPA_PSK)
