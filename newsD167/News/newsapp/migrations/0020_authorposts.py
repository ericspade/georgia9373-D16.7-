# Generated by Django 3.2.13 on 2023-11-07 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0019_remove_comments_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.post')),
            ],
        ),
    ]
