# Generated by Django 3.1.7 on 2021-02-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210223_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoList',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
        migrations.AddField(
            model_name='todo',
            name='items',
            field=models.TextField(default='[]'),
        ),
    ]
