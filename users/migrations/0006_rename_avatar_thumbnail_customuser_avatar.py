# Generated by Django 4.0 on 2022-10-12 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_customuser_avatar_customuser_avatar_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='avatar_thumbnail',
            new_name='avatar',
        ),
    ]