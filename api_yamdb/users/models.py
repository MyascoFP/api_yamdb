from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):
    ROLE = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        choices=ROLE,
        max_length=max(len(role[1]) for role in ROLE), default=USER
    )

    email = models.EmailField(
        'Электронная почта',
        unique=True,
        max_length=254,
    )

    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
        null=True
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def is_admin(self):
        return (
            self.role == ADMIN
            or self.is_superuser
        )

    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username
