from django.urls import re_path
from .streamer import CoordinatesStreamer
# from channels.routing import ProtocolTypeRouter, URLRouter

# application = ProtocolTypeRouter({
#     "websocket": URLRouter(
#         [
#             re_path(r'ws/mission_execution/$', MissionExecutionManager.as_asgi()),
#             # Add other WebSocket consumers and paths as needed
#         ]
#     ),
# })

# websocket_urlpatterns = [
#     re_path(r'ws/mission_execution/$', MissionExecutionManager.as_asgi()),
# ]

websocket_urlpatterns = [
    re_path('ws/coordinates/', CoordinatesStreamer.as_asgi()),
]