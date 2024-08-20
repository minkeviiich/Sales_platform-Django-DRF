from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from courses.models import Course
from django.core.exceptions import ValidationError

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
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'balance'):
            Balance.objects.create(user=self)
    
    
class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='balance'
    )
    balance = models.PositiveIntegerField(default=1000)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValidationError('Баланс не может быть ниже 0.')
        super().save(*args, **kwargs)

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
    start_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подписки'
    )
    end_at = models.DateTimeField(
        verbose_name='Дата окончания подписки',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(fields=['user',  'course'], name='unique_subscription')
        ]
    
    

