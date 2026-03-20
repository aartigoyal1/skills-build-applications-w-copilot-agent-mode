from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data (delete individually for MongoDB compatibility)
        for model in [app_models.Activity, app_models.Workout, app_models.Leaderboard, app_models.UserProfile, app_models.Team]:
            # Delete only objects with a valid id
            model.objects.exclude(id=None).delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users
        users = [
            app_models.UserProfile.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.UserProfile.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            app_models.UserProfile.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.UserProfile.objects.create(name='Batman', email='batman@dc.com', team=dc),
            app_models.UserProfile.objects.create(name='Superman', email='superman@dc.com', team=dc),
            app_models.UserProfile.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        for user in users:
            for i in range(3):
                app_models.Activity.objects.create(user=user, description=f"Activity {i+1} for {user.name}", duration=30+i*5)

        # Create Workouts
        for user in users:
            app_models.Workout.objects.create(user=user, name=f"Workout for {user.name}", difficulty='Medium')

        # Create Leaderboard
        for team in [marvel, dc]:
            app_models.Leaderboard.objects.create(team=team, score=100 if team.name == 'Team Marvel' else 90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
