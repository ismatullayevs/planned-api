# Generated by Django 4.1.1 on 2022-09-30 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_todo_nanoid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='nanoid',
        ),
    ]
