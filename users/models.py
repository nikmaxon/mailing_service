from django.contrib.auth.models import AbstractUser, Group
from django.db import models


NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def add_mailing_group(self):
        mailing_group = Group.objects.get(name='manager_mailing')
        if self.groups.filter(id=mailing_group.id).exists():
            self.groups.add(mailing_group)
