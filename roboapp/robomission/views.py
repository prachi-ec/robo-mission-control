from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Mission

@csrf_exempt
@require_POST
def add_mission(request):
    mission_name = request.GET.get('mission_name', '')
    if mission_name:
        mission = Mission.objects.create(name=mission_name)

        return JsonResponse({
            'mission': mission.name,
            'msg': f'added {mission.name} successfully',
        }, status=201)
    else:
        return JsonResponse({'error': 'Mission name is required'}, status=400)