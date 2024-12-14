from rest_framework.serializers import ModelSerializer
from users.models import User
from habits.serializers import HabitSerializer


class UserSerializer(ModelSerializer):
    habits = HabitSerializer(source='users_habits', many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
