# Generated by Django 2.2 on 2019-08-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20190804_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='reply_counts',
        ),
        migrations.AddField(
            model_name='topic',
            name='comment_counts',
            field=models.IntegerField(default=0, verbose_name='话题评论数'),
        ),
    ]
