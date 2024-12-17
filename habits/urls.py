from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import PrivateHabitViewSet, PublicHabitViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'my-habits', PrivateHabitViewSet, basename='my_habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public_habits')

urlpatterns = [
    path('', include(router.urls)),
]
