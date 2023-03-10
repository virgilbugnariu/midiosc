import json

class Connection:
    def __init__(self, data):
        self.config = None
        self.data = data

        
    def init(self):
        self.read_config()
        self.add_address_to_config(self.data)
        self.save_config()

    def read_config(self):
        with open('config.json', 'r') as file_handle:
            self.config = json.load(file_handle)

    def add_address_to_config(self, value):
        self.config['address'] = value
    
    def save_config(self):
        json_str = json.dumps(self.config)
        with open("config.json", "w") as f:
            f.write(json_str)