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
    path('habits/', HabitListAPIView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits_retrieve'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habits_delete'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habits_update'),
]

urlpatterns += router.urls
