from pythonosc import udp_client
import random
import time
import json
import mido

class Start:
    def __init__(self):
        print("Start")

        self.config = None
        self.device = None
        self.client = None
        self.running = True

    def init(self):
        self.read_config()

        self.client = udp_client.SimpleUDPClient("127.0.0.1", 5005)
        self.device = mido.open_input(self.config["device_name"])

        self.listen()


    def read_config(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f) 

    def listen(self):
        try:
            while self.running:
                if self.device.poll():
                    msg = self.device.receive()
                    self.handle_message(msg)
        except KeyboardInterrupt:
            self.running = False
            return

    def handle_message(self, message):
        for key in self.config['messages']:
            for sub_key, sub_value in self.config['messages'][key].items():
                if isinstance(sub_value, dict) and sub_value.get('note') == message.note:
                    print(f"Found {key}.{sub_key}")
                    self.client.send_message("/deck/" + key + "/" + sub_key, 1)
                    time.sleep(0.1)
                    self.client.send_message("/deck/" + key + "/" + sub_key, 0)