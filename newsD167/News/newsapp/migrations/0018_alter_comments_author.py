# Generated by Django 3.2.13 on 2023-11-07 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0017_alter_comments_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newsapp.post'),
        ),
    ]
