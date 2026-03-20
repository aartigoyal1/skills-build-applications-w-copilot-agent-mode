from rest_framework import serializers
from .models import UserProfile, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if value else None
    def to_internal_value(self, data):
        return ObjectId(data) if data else None

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    team = ObjectIdField()
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    class Meta:
        model = Activity
        fields = ['id', 'user', 'description', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'difficulty']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    team = ObjectIdField()
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'score']
