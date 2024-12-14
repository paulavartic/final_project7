from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class PrivateHabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class PublicHabitViewSet(ReadOnlyModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(public=True)

