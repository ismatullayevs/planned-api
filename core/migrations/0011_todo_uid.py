# Generated by Django 4.0 on 2022-10-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_todo_options_todo_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='uid',
            field=models.CharField(default='slkdjf;asl', max_length=30, verbose_name='UID'),
            preserve_default=False,
        ),
    ]
