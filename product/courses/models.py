from django.db import models
from django.utils import timezone

class Course(models.Model):
    """Модель продукта - курса."""
    
    author = models.ForeignKey(
        'users.CustomUser',  
        on_delete=models.DO_NOTHING, 
        verbose_name='Автор'
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )
    price = models.FloatField(
        default=0.0,
        verbose_name='Цена'
    )
    created_at = models.DateTimeField(
        default=timezone.now, 
        verbose_name='Дата публикации'
    )
   
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель урока."""
    
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        verbose_name='Курс',
        related_name='lessons'
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название урока',
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель группы."""
    
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        verbose_name='Курс'
    )
    title = models.CharField(
        max_length=100, 
        verbose_name='Название группы'
    )
    students = models.ManyToManyField(
        'users.CustomUser', 
        verbose_name='Студенты'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)
