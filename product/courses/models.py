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
        verbose_name='Дата и время начала курса',
        null=False,
        blank=False
    )
    end_date = models.DateTimeField(
        verbose_name='Дата и время окончания курса',
        null=False,
        blank=False
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена'
    )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_groups()

    def create_groups(self):
        for i in range(1, 11):
            Group.objects.create(course=self, title=f'Группа {i}')
   
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
        verbose_name='Курс',
        related_name='groups'
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
