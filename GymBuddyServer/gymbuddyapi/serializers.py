from rest_framework import serializers
from .models import Account, Exercise, Workout


class AccountSerializer(serializers.ModelSerializer):
    # exercises = serializers.PrimaryKeyRelatedField(many=True, queryset=Exercise.objects.all())

    class Meta:
        model = Account
        fields = ['id','first_name', 'last_name', 'username', 'password', 'email']
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'exercise_type', 'datetime', 'account', 'video_file', 'csv_file']
    
    id = serializers.IntegerField(read_only=True)
    exercise_type = serializers.CharField()
    datetime = serializers.DateTimeField()
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    video_file = serializers.FileField()
    csv_file = serializers.FileField()

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'account', 'startTime', 'endTime']

    id = serializers.IntegerField(read_only=True)
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
