from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from courses.models import Course

class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()
    
class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='balance'
    )
    balance = models.PositiveIntegerField(default=1000)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    course = models.ForeignKey(
        Course, 
        related_name='subscriptions',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser, 
        related_name='subscriptions',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        default=timezone.now, 
        verbose_name='Дата публикации'
    )
    is_paid = models.BooleanField(default=False) 

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(fields=['user',  'course'], name='unique_subscription')
        ]
    
    

