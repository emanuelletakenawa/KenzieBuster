# Generated by Django 4.2.6 on 2023-10-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]