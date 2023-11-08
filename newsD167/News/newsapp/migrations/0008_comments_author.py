# Generated by Django 3.2.13 on 2023-11-07 06:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='newsapp.post'),
            preserve_default=False,
        ),
    ]