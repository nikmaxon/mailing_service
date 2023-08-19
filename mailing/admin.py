from django.contrib import admin

from mailing.models import Mailing, Log, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'status')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('date_attempt', 'status', 'answer')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')

