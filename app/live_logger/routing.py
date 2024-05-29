from django.urls import path, re_path, include
from . import consumers

websocket_urlpatterns = [
    path('ws/live_logger/logs/', consumers.LogConsumer.as_asgi())
]