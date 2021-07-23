''' from channels.consumer import SyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, async_to_sync


class EchoConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, text_data):
        self.send({
            'type': "send.msg",
            'text': text_data,
        })


    def send_msg(self,event):
        self.send(event['text'])
    
    def websocket_disconnect(self, event):
        print('Disconnected', event) '''


''' from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, async_to_sync, AsyncConsumer
from channels.layers import get_channel_layer
import json '''

''' class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.group_name='data'
        await self.channel_layer.group_add(
            'data',
            self.channel_name
        )        
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_disconnect(self,close_code):
        print('Disconnected', close_code)
        self.group_name='data'
        await self.channel_layer.group_discard(
            'data',
            self.channel_name
        )

    async def websocket_receive(self,text_data):
        print(text_data)
        group_name='data'
        await self.channel_layer.group_send(
            'data',
            {
                'type' : 'send_msg',
                'value' : text_data,
            }
        )

    async def send_msg(self,event):
        print(event['value'])
        print('------')
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps(event['value']),
        })
        print('sent')
        print(json.dumps(event['value'])) '''

from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, async_to_sync, AsyncConsumer
from channels.layers import get_channel_layer
import json


class Data(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name='data'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )        
        await self.accept()

    async def disconnect(self,close_code):
        print('Disconnected', close_code)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self,text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'send.msg',
                'value':text_data,
            }
        )

    async def send_msg(self,event):        
        await self.send(event['value'])


class Command(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name='cmd'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )        
        await self.accept()

    async def disconnect(self,close_code):
        print('Disconnected', close_code)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self,text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'send.msg',
                'value':text_data,
            }
        )

    async def send_msg(self,event):        
        await self.send(event['value'])