# missions/tasks.py
from celery import shared_task
import time
from .models import Mission

@shared_task
def execute_mission(mission_id):
    mission = Mission.objects.get(id=mission_id)
    print(f"I am mission: {mission.name}")
    
    mission.set_executing()
    for _ in range(3):
        time.sleep(20)
        print(f"I am mission: {mission.name} - Executing...")

    mission.set_completed()
    return True