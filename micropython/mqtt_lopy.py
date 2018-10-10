import time
import sys

if sys.platform == 'LoPy4':
    from mqtt import MQTTClient

if sys.platform == 'esp32':
    def install_umqtt_lib():
        import upip
        upip.install('micropython-umqtt.robust')

    from umqtt.robust import MQTTClient


def sub_cb(topic, msg):
    print(msg)


client = MQTTClient("device_id", "io.adafruit.com", user="your_username", password="your_api_key", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="youraccount/feeds/lights")

while True:
    print("Sending ON")
    client.publish(topic="youraccount/feeds/lights", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="youraccount/feeds/lights", msg="OFF")
    client.check_msg()

    time.sleep(1)
from umqtt.simple import MQTTClient
