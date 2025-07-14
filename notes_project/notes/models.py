from django.db import models
class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    understanding = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Понятность')

    def __str__(self):
        return self.title
# Create your models here.
