from channels.generic.websocket import AsyncWebsocketConsumer
from django.core import serializers
from asgiref.sync import async_to_sync, sync_to_async
from .models import Log
from pprint import pprint
import json
from . import settings
from .serializers import LogSerializer

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if not self.scope['user'].is_staff:
            await self.close()
            return
        print(self.scope['user'])
        await self.accept()
        logs = await sync_to_async(self.fetch_logs)()
        # await self.send(json.dumps({'type': 'logs', 'data': logs}))
        await self.send(json.dumps({'type': 'logs', 'data': logs}))

    def fetch_logs(self, start=0, end=settings.LIVE_LOGGER_PAGINATION) -> dict:
        logs = Log.objects.all().order_by('-id').prefetch_related('location', 'user')[start:end]
        return LogSerializer(logs, many=True).data

    async def disconnect(self, close_code):
        print('Disconnected!')

    async def receive(self, text_data):
        print('Received:', text_data) 