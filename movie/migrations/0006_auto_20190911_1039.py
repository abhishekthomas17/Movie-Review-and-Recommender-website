# Generated by Django 2.2.4 on 2019-09-11 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20190911_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='helpful',
        ),
        migrations.RemoveField(
            model_name='review',
            name='number_helpful',
        ),
    ]