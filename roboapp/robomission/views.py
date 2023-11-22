from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Mission
from .models import Mission
from .tasks import execute_mission
from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

def view_missions(request):
    missions = Mission.objects.all()
    return render(request, 'missions.html', {'missions': missions})

def view_coordinates(request):
    # we will get the chatbox name from the url
    return render(request, "coordinates.html", {"data": "coordinates"})

@csrf_exempt
@require_POST
def add_mission(request):
    try:
        mission_name = request.GET.get('mission_name', '')

        if mission_name:
            mission = Mission.objects.create(name=mission_name)
            res = execute_mission.delay(mission.id)
    
            channel_layer = get_channel_layer()
            res1 =async_to_sync(channel_layer.group_send)(
                "mission_coordinates",  # Replace with the actual WebSocket group name
                {"type": "mission_coord", "message": f"MC: I am called! finally! {mission.name}"}
            )
            print(res1)
            return JsonResponse({'status': 'Mission added to the queue'})
        else:
            return JsonResponse({'status': 'Invalid request'}, status=400)
    except Exception as e:
        return JsonResponse(data=e.__dict__(),status=500)