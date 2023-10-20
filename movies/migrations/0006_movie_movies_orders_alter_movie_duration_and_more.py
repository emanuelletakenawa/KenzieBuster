# Generated by Django 4.2.6 on 2023-10-13 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_orders', '__first__'),
        ('movies', '0005_alter_movie_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movies_orders',
            field=models.ManyToManyField(related_name='order', through='movies_orders.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(blank=True, default=''),
        ),
    ]