from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import (HabitViewSet,
                          HabitListAPIView,
                          HabitCreateAPIView,
                          HabitUpdateAPIView,
                          HabitRetrieveAPIView,
                          HabitDestroyAPIView)

app_name = HabitsConfig.name

router = SimpleRouter()
router.register('', HabitViewSet)

urlpatterns = [
    path('habits/', HabitViewSet.as_view(), name='habits_list'),
   ]

urlpatterns += router.urls
