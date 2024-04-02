# Generated by Django 5.0.3 on 2024-04-02 09:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_rating_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user_id', 'movie_id')},
        ),
    ]