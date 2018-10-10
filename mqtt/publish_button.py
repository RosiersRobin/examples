import uuid
from signal import pause

from gpiozero import Button
from paho.mqtt.client import Client as MQTTClient

from settings import Settings


class ButtonPublisher(MQTTClient):
    def __init__(self, button, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = button

    def on_connect(self):
        self.button.when_pressed = lambda: self.publish("/buttons/{}/pressed".format(pin))
        self.button.when_released = lambda: self.publish("/buttons/{}/released".format(pin))

    def on_disconnect(self):
        self.button.when_pressed = lambda: None
        self.button.when_released = lambda: None


if __name__ == "__main__":
    pin = 13
    btn = Button(pin)

    client = ButtonPublisher(btn, client_id=uuid.uuid4())
    client.connect(Settings.MQTT_BROKER, Settings.MQTT_PORT)

    pause()
