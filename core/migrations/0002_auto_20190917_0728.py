# Generated by Django 2.2.5 on 2019-09-17 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='ratings',
            new_name='rating',
        ),
    ]
