from pythonosc import udp_client
import random
import time
import json
import mido

PORT = 5005

class Start:
    def __init__(self):
        print("Start")

        self.config = None
        self.device = None
        self.client = None
        self.running = True

    def init(self):
        self.read_config()

        self.client = udp_client.SimpleUDPClient(self.config["address"], PORT)
        self.device = mido.open_input(self.config["device_name"])

        self.listen()


    def read_config(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f) 

    def listen(self):
        try:
            while self.running:
                msg = self.device.receive()
                if msg.type == 'note_on':
                    self.handle_message(msg)
        except KeyboardInterrupt:
            self.running = False
            return

    def handle_message(self, message):
        if message.channel == 0 or message.channel == 1:
            channel_to_deck = "a" if message.channel == 0 else "b"
            if message.note == 1:
                # Handle CUE
                self.client.send_message("/deck/" + channel_to_deck + "/cue", 1 if message.velocity == 127 else 0)
                return
            if message.note == 0:
                # Handle PLAY
                self.client.send_message("/deck/" + channel_to_deck + "/play", 1 if message.velocity == 127 else 0)
                return