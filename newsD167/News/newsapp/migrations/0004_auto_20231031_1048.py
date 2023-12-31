# Generated by Django 3.2.13 on 2023-10-31 16:48

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0003_auto_20220713_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.TextField(help_text='category name', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.author', verbose_name='help text'),
        ),
    ]
