
from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', db_column='team_id', to_field='id')
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities', db_column='user_id', to_field='id')
    description = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return f"{self.description} ({self.user.name})"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts', db_column='user_id', to_field='id')
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} ({self.user.name})"

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards', db_column='team_id', to_field='id')
    score = models.IntegerField()
    def __str__(self):
        return f"{self.team.name}: {self.score}"
