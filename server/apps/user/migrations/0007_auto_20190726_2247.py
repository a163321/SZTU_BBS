# Generated by Django 2.2 on 2019-07-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别'),
        ),
    ]