# Generated by Django 4.2 on 2023-06-05 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='accuracy',
            new_name='top_accuracy',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='top_overall',
            new_name='top_time',
        ),
    ]
