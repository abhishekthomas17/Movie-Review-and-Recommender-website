# Generated by Django 2.2.4 on 2019-09-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190907_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]