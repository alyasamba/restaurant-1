# Generated by Django 2.1.5 on 2020-06-09 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_auto_20200609_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
    ]