from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class PrivateHabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class PublicHabitViewSet(ReadOnlyModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(habit_status='Public')
