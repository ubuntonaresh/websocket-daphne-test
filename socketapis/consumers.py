from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send('Connected')

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(f'Send message: {text_data}')