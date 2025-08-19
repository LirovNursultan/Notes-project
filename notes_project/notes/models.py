from django.db import models

class Note(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'IT'),
        ('Языки', 'Языки'),
    ]

    SUBCATEGORY_CHOICES = [
        ('Веб-разработка', 'Веб-разработка'),
        ('Компьютерная безопасность', 'Компьютерная безопасность'),
        ('Компьютерные сети', 'Компьютерные сети'),
        ('Python', 'Python'),
        ('C++', 'C++'),

        ('Английский', 'Английский'),
        ('Корейский', 'Корейский'),
        ('Японский', 'Японский')
    ]

    title = models.CharField(max_length=255, verbose_name='Тема')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Категория')
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES, verbose_name='Подкатегория')

    description = models.TextField(verbose_name='Описание')
    understanding = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Понятность')
    what_learned = models.TextField(blank=True, null=True, verbose_name='Что я изучил нового')
    what_not_understood = models.TextField(blank=True, null=True, verbose_name='Что непонятно')

    def __str__(self):
        return self.title

