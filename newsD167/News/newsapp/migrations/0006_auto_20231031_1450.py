# Generated by Django 3.2.13 on 2023-10-31 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20231031_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, unique=True)),
                ('comment_text', models.TextField(max_length=500)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='newsapp.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]