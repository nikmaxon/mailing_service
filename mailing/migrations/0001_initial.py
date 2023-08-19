# Generated by Django 4.2.4 on 2023-08-19 16:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attempt', models.DateTimeField(verbose_name='Дата попытки')),
                ('status', models.CharField(max_length=150, verbose_name='Статус попытки')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='тема сообщения')),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время рассылки')),
                ('periodicity', models.PositiveSmallIntegerField(choices=[(1, 'Раз в день'), (2, 'Раз в неделю'), (3, 'Раз в месяц')], default=1, verbose_name='периодичность')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Создана'), (2, 'Запущена'), (3, 'Завершена')], default=1, verbose_name='статус рассылки')),
                ('massage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.message')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]