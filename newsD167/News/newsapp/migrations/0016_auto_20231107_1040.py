# Generated by Django 3.2.13 on 2023-11-07 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0015_rename_author_comments_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='auth',
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
