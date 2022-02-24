from cgitb import text
from datetime import date
from tabnanny import verbose
from django.utils import timezone
from django.db import models

class News(models.Model):
    title = models.CharField('Title', max_length=80)
    preview = models.CharField('Preview', max_length=140)
    textNews = models.TextField('Main news')

    def __str__(self):
        return self.title

class Todo(models.Model):
    tasktodo = models.CharField(max_length=50)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tasktodo


    # title = models.CharField('Название', max_length=50)
    # task = models.TextField('Oписание')

    # def __str__(self):
    #     return self.title

    #     class Meta:
    #         verbose_name = 'Task'
    #         verbose_name_plural = 'Tasks'