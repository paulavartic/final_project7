from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(
        verbose_name="Email",
        help_text="Your email",
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='Name',
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
        **NULLABLE
    )
    tg_chat_id = models.PositiveIntegerField(
        verbose_name='Telegram chat ID',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('id',)

    def __str__(self):
        return self.email
