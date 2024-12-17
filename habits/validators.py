from django.utils import timezone
from rest_framework import serializers

from habits.models import Habit


class RewardAndRelatedValidator:
    def __call__(self, value):
        if value.get('reward') and value.get('related'):
            raise serializers.ValidationError(
                'You can not fill in both this fields, you can only choose one.'
            )


class ExecutionTimeValidator:
    def __call__(self, value):
        if value.get('duration', 0) > 2:
            raise serializers.ValidationError(
                'Duration can not be shorter than 2 mins.'
            )


class EnjoyableHabitValidator:
    def __call__(self, value):
        related_id = value.get('related_habit')
        if related_id:
            related_habit = Habit.objects.filter(id=related_id).first()
            if related_habit and not related_habit.enjoyable_habit_indicator:
                raise serializers.ValidationError(
                    'Related habit has to have a enjoyable indicator.'
                )


class PleasantHabitNoRelatedOrPrizeValidator:
    def __call__(self, value):
        if value.get('enjoyable_habit_indicator') and (value.get('reward') or value.get('related_habit')):
            raise serializers.ValidationError(
                'An enjoyable habit can not have a prize or a related habit.'
            )


class FrequencyValidator:
    def __call__(self, value):
        if value.get('frequency', 0) > 7:
            raise serializers.ValidationError(
                'You have to perform the habit at least once in 7 days.'
            )
