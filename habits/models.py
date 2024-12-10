from datetime import timedelta

from django.db import models

from users.models import NULLABLE, User


class Habit(models.Model):
    """Habit model."""
    name = models.CharField(
        max_length=200,
        verbose_name='Name',
    )
    place = models.CharField(
        max_length=200,
        verbose_name='Place where the habit is performed',
        **NULLABLE
    )
    time = models.TimeField(
        verbose_name='Time when the habit has to be performed',
        **NULLABLE
    )
    enjoyable_habit_indicator = models.BooleanField(
        verbose_name='Indicator of a enjoyable habit',
        default='False'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Related enjoyable habit',
        **NULLABLE,
    )
    frequency = models.PositiveSmallIntegerField(
        verbose_name='Frequency of performance',
        default=1,
    )
    reward = models.CharField(
        max_length=200,
        verbose_name='Reward for performing the habit',
        **NULLABLE
    )
    duration = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name='Time to spend on the habit',
    )
    PUBLIC_STATUS = [
        ('Pubic', 'Public'),
        ('Private', 'Private'),
    ]
    habit_status = models.CharField(
        max_length=50,
        verbose_name='Habit status',
        choices=PUBLIC_STATUS,
        default='Private',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Habit owner',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'

    def __str__(self):
        return self.name
