# Generated by Django 4.1.1 on 2023-03-19 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
