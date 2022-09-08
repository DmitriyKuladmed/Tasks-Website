from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=250)
    task = models.TextField('Описание')
    time_of_create = models.DateTimeField(auto_now_add=True)
    email = models.EmailField('Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
