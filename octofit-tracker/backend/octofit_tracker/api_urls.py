from django.urls import path
from django.http import JsonResponse

def users(request):
    return JsonResponse({'message': 'Users endpoint'})

def teams(request):
    return JsonResponse({'message': 'Teams endpoint'})

def activities(request):
    return JsonResponse({'message': 'Activities endpoint'})

def leaderboard(request):
    return JsonResponse({'message': 'Leaderboard endpoint'})

def workouts(request):
    return JsonResponse({'message': 'Workouts endpoint'})

urlpatterns = [
    path('users/', users),
    path('teams/', teams),
    path('activities/', activities),
    path('leaderboard/', leaderboard),
    path('workouts/', workouts),
]
