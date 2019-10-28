# Generated by Django 2.2.4 on 2019-10-06 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20190828_1333'),
        ('game', '0003_user_in_room_is_room_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_sign_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='签到时间')),
                ('content', models.CharField(default='', max_length=100, verbose_name='对自己说的话')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Room', verbose_name='签到的房间id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '用户每日签到表',
                'verbose_name_plural': '用户每日签到表',
            },
        ),
        migrations.CreateModel(
            name='Sign_in_room_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='开始时间')),
                ('date_end', models.DateTimeField(verbose_name='结束时间')),
                ('time_start', models.IntegerField(default=0, verbose_name='签到开始时间')),
                ('time_end', models.IntegerField(default=0, verbose_name='签到结束时间')),
                ('during', models.IntegerField(default=0, verbose_name='持续天数')),
                ('alert', models.CharField(default='', max_length=50, verbose_name='打卡宣言')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Room', verbose_name='签到的房间id')),
            ],
            options={
                'verbose_name': '房间打卡信息表',
                'verbose_name_plural': '房间打卡信息表',
            },
        ),
    ]