# Generated by Django 5.0.6 on 2024-06-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_genre_songmodel_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='SongGenre',
        ),
    ]
