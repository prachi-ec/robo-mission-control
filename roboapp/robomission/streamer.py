import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class CoordinatesStreamer(WebsocketConsumer):
    def connect(self):
        self.room_name = "coordinates"
        self.room_group_name = f'mission_{self.room_name}'

        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,  # Replace with the actual WebSocket group name
            self.channel_name #read only, don't set channel_name
        )

        print("connected")

    def disconnect(self, code):
        print("disconnected")

    def send_message(self, message):
        self.send(text_data=json.dumps({
            'message': message
        }))

    def receive(self, text_data):
        self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'mission_coord',
                        'message': text_data,
                    })
    
    def mission_coord(self, event):
        self.send(text_data=json.dumps(event["data"]))