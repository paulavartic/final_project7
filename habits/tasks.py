from celery import shared_task
from habits.models import Habit
import datetime
from habits.services import send_telegram_message


@shared_task
def send_reminder():
    """Sends reminders about habits to the user."""
    habits = Habit.objects.filter(enjoyable_habit_indicator=False)
    for habit in habits:
        if habit.time >= current_date:
            tg_chat = habit.user.tg_chat_id
            message = f'I will {habit.name} at {habit.time} at {habit.place}.'
            send_telegram_message(tg_chat, message)
