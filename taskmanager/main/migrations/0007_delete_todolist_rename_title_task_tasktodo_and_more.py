# Generated by Django 4.0.1 on 2022-02-14 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_todolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ToDoList',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='tasktodo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='preview',
        ),
        migrations.RemoveField(
            model_name='task',
            name='text',
        ),
    ]
