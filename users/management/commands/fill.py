from django.core.management import BaseCommand
from django.utils import timezone

from client.models import Client
from mailing.models import Mailing, Message
from users.models import User

"""Команда для наполнения базы Рассылки, Клиенты, Сообщения"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        message_list = [
            {'id': 3, 'theme': 'Оставайтесь на связи',
             'body': 'Оставайтесь на связи с теми, кто Вам дорог, и не пропускайте важные обсуждения. Отправляйте неограниченное количество текстовых сообщений, фото, видео, документов и другого контента на любые устройства iOS, iPadOS, macOS или watchOS через iMessage или обменивайтесь SMS- и MMS-сообщениями.'},
            {'id': 2, 'theme': 'Купите курс скайпро', 'body': 'купи и приведи друга'}
        ]
        message_for_create = []

        for message in message_list:
            message_for_create.append(
                Message(**message)
            )

        Message.objects.bulk_create(message_for_create)

        mailing_list = [
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 2, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 3, 'massage': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'massage': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3},
        ]
        mailing_for_create = []

        for mailing in mailing_list:
            mailing_for_create.append(
                Mailing(**mailing)
            )

        Mailing.objects.bulk_create(mailing_for_create)

        client_list = [
            {'first_name': 'Ivan', 'last_name': 'Ivanov', 'second_name': 'Ivanovich', 'email': 'test1@sky.pro'},
            {'first_name': 'Petr', 'last_name': 'Petrov', 'second_name': 'Petrovich', 'email': 'test2@sky.pro'},
            {'first_name': 'Serg', 'last_name': 'Sergeev', 'second_name': 'Sergeevich', 'email': 'test3@sky.pro'},
            {'first_name': 'Olegka', 'last_name': 'Olegov', 'second_name': 'Olegovich', 'email': 'test4@sky.pro'},
            {'first_name': 'Igor', 'last_name': 'Igorev', 'second_name': 'Igorevich', 'email': 'test5@sky.pro'},
            ]
        client_for_create = []

        for client in client_list:
            client_for_create.append(
                Client(**client)
            )

        Client.objects.bulk_create(client_for_create)


