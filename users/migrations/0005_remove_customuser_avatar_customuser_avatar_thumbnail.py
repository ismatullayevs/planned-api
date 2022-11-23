# Generated by Django 4.0 on 2022-10-12 06:42

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='avatars'),
        ),
    ]