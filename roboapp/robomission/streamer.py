# robomission/consumers.py
import json
import time
import asyncio
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class CoordinatesStreamer(WebsocketConsumer):
    def connect(self):
        #self.group_name = 'coordinates'


        self.room_name = "coordinates"
        self.room_group_name = f'mission_{self.room_name}'


        print()
        print()
        print(" ----------- connecting --------------")
        print()
        self.accept()
        result = async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,  # Replace with the actual WebSocket group name
            self.channel_name #read only, don't set channel_name
        )

        print("result of group add: ", result)
        self.send(f"I am {self.channel_name} connected")
        print(f"{self.channel_layer} - {self.groups}")
        print("connected")

    def disconnect(self, code):
        # Leave mission group
        print()
        print()
        print(" ----------- disconnecting --------------")
        print()
        print()
        print("disconnected")

    def send_message(self, message):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def stream_messages(self, mission):
        file_path = r"C:\Users\Nakshata\Downloads\mission1.txt"
        for i in range(5):
            self.send_message(f"I am called! finally! {mission}-{i}")
        # while True:
        #     with open(file_path) as file:
        #         for line in file:
        #             coordinates = json.loads(line)
        #             await self.send_coordinates({"coordinates": coordinates})
        #             await asyncio.sleep(2)

    def receive(self, text_data):
        print()
        print()
        print(f" ----------- recived something {text_data} --------------")
        print()
        print()
        self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'mission_coord',
                        'message': text_data,
                    })
    
    def mission_coord(self, event):
        print(f"mission coord triggered: {event}")

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))