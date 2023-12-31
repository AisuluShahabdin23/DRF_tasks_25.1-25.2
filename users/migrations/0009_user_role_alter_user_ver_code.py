# Generated by Django 5.0 on 2023-12-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_ver_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='382487865041', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
