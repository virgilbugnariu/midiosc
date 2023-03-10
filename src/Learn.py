import json
import mido

class Learn:
    def __init__(self):
        print("Learn mode started")

        self.running = True

        self.device = None

        self.messages = {
            "a": {
                "cue": None,
                "play": None
            },
            "b": {
                "cue": None,
                "play": None
            }
        }

    def init(self):
        self.device = self.select_device()
        self.listen()
    
    def select_device(self):
        print("Select the target device")
        all_inputs = mido.get_input_names()

        for inputIndex, inputDevice in enumerate(all_inputs):
            print("(", inputIndex, ")", inputDevice)

        target_device_index = input("Target device: ")

        return mido.open_input(all_inputs[int(target_device_index)])

    def listen(self):
        print("Press the following buttons: DECK A CUE, DECK A PLAY, DECK B CUE, DECK B PLAY")
        try:
            while self.running:
                if self.device.poll():
                    msg = self.device.receive()
                    if self.messages["a"]["cue"] is None:
                        self.deck_learn("a", "cue", msg)
                    elif self.messages["a"]["play"] is None:
                        self.deck_learn("a", "play", msg)
                    elif self.messages["b"]["cue"] is None:
                        self.deck_learn("b", "cue", msg)
                    elif self.messages["b"]["play"] is None:
                        self.deck_learn("b", "play", msg)

                    all_selected = all(val2 is not None for val1 in self.messages.values() for val2 in val1.values())
                    if all_selected:
                        self.device.close()
                        self.store_preferences()
                        break
            
            print("All keys stored")
        except KeyboardInterrupt:
            self.running = False
            return
    
    def deck_learn(self, deck, type, msg):
        print("Stored", type, "on", deck)
        self.messages[deck][type] = vars(msg)

    def store_preferences(self):
        config = {
            "device_name": self.device.name,
            "messages": self.messages,
            "address": ""
        }
        json_str = json.dumps(config)
        with open("config.json", "w") as f:
            f.write(json_str)

