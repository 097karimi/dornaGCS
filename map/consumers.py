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