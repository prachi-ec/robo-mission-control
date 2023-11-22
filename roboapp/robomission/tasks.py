from celery import shared_task
import time
from .models import Mission
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import os
from django.conf import settings

@shared_task
def execute_mission(mission_id):
    mission = Mission.objects.get(id=mission_id)
    mission.set_executing()

    channel_layer = get_channel_layer()
    file_path = os.path.join(settings.BASE_DIR, f'{mission.name}.txt')

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                cleaned_line = line.strip()
                async_to_sync(channel_layer.group_send)(
                    "mission_coordinates",
                    {"type": "mission_coord", "data": cleaned_line}
                )

                time.sleep(0.01)
    except Exception as e:
        async_to_sync(channel_layer.group_send)(
                    "mission_coordinates",
                    {"type": "mission_coord", "data": f"failure streaming coordinates for mission {mission.name} - {e}"}
                )

    mission.set_completed()
    return True