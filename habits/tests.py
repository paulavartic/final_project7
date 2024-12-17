from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from datetime import time
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.validators import RewardAndRelatedValidator
from users.models import User


class HabitModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name='test1', email='test1@mail.com', password='1testpass')

    def test_create_habit(self):
        habit = Habit.objects.create(
            owner=self.user,
            name='Test Habit',
            place='Home',
            duration=30,
            time=timezone.now().time(),
            enjoyable_habit_indicator=False
        )
        self.assertEqual(habit.name, 'Test Habit')
        self.assertEqual(habit.owner, self.user)
        self.assertFalse(habit.enjoyable_habit_indicator)


class HabitSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name='test', email='testuser@mail.com', password='testpass')

    def test_valid_data(self):
        data = {
            'owner': self.user.id,
            'name': 'Test Habit',
            'place': 'Home',
            'duration': 2,
            'time': time(12, 0),
            'enjoyable_habit_indicator': False
        }
        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid(), f"Errors: {serializer.errors}")

    def test_invalid_data(self):
        data = {
            'owner': self.user.id,
            'name': '',
            'place': 'Home',
            'duration': -10,
            'time': '25:00:00',
            'enjoyable_habit_indicator': False
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        self.assertIn('name', serializer.errors)

        self.assertIn('duration', serializer.errors)
        self.assertIn('Make sure the value is more than 0.', serializer.errors['duration'])

        self.assertIn('time_action', serializer.errors)


class RewardAndRelatedValidatorTest(TestCase):

    def setUp(self):
        self.validator = RewardAndRelatedValidator()
        self.user = User.objects.create_user(first_name='test3', email='testuser3@mail.com', password='testpass3')

    def test_both_prize_and_related(self):
        data = {
            'reward': 'Reward',
            'related_habit': 1
        }
        with self.assertRaisesMessage(
                Exception,
                'You need to choose one option only.'
        ):
            self.validator(data)

    def test_only_prize(self):
        data = {
            'reward': 'Reward',
            'related': None
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    def test_only_related(self):
        data = {
            'reward': None,
            'related': 1
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')


class MyHabitsViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(first_name='test4', email='testuser4@mail.com', password='testpass4')

        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')


def test_get_my_habits(self):
    Habit.objects.create(
        owner=self.user,
        name='Habit 1',
        place='Home',
        duration=30,
        time=timezone.now().time(),
        enjoyable_habit_indicator=False
    )
    Habit.objects.create(
        owner=self.user,
        name='Habit 2',
        place='Work',
        duration=45,
        time=timezone.now().time(),
        enjoyable_habit_indicator=True
    )

    url = reverse('habits:my_habits-list')
    response = self.client.get(url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)


def test_create_habit(self):
    url = reverse('habits:my_habits-list')
    data = {
        'name': 'New Habit',
        'place': 'Gym',
        'duration': 60,
        'time': '12:00:00',
        'enjoyable_habit_indicator': False
    }
    response = self.client.post(url, data, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Habit.objects.count(), 1)
    self.assertEqual(Habit.objects.get().name, 'New Habit')
    self.assertEqual(Habit.objects.get().owner, self.user)
