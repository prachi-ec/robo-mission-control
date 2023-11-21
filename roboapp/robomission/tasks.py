# missions/tasks.py
from celery import shared_task
import time
from .models import Mission

@shared_task
def execute_mission(mission_id):
    for _ in range(5):
        time.sleep(2)
        print(f"I am mission: {mission_id} - Executing...")
    return True