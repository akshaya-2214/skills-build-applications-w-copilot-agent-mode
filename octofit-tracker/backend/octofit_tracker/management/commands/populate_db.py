from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        app_models.Leaderboard.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Workout.objects.all().delete()
        app_models.Team.objects.all().delete()
        get_user_model().objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users (Superheroes)
        users = [
            {'email': 'tony@marvel.com', 'username': 'ironman', 'team': marvel},
            {'email': 'steve@marvel.com', 'username': 'captainamerica', 'team': marvel},
            {'email': 'bruce@marvel.com', 'username': 'hulk', 'team': marvel},
            {'email': 'clark@dc.com', 'username': 'superman', 'team': dc},
            {'email': 'bruce@dc.com', 'username': 'batman', 'team': dc},
            {'email': 'diana@dc.com', 'username': 'wonderwoman', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = get_user_model().objects.create_user(email=u['email'], username=u['username'], password='password', team=u['team'])
            user_objs.append(user)

        # Create Workouts
        workout1 = app_models.Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = app_models.Workout.objects.create(name='Running', description='Cardio endurance')
        workout3 = app_models.Workout.objects.create(name='Squats', description='Lower body strength')

        # Create Activities
        for user in user_objs:
            app_models.Activity.objects.create(user=user, workout=workout1, duration=30, calories=200)
            app_models.Activity.objects.create(user=user, workout=workout2, duration=20, calories=150)
            app_models.Activity.objects.create(user=user, workout=workout3, duration=15, calories=100)

        # Create Leaderboard
        for team in [marvel, dc]:
            app_models.Leaderboard.objects.create(team=team, points=1000 if team.name == 'Team Marvel' else 900)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
