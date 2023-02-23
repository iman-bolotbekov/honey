import math
from random import random

from django.db import models
from django.contrib.auth.models import User

from .utils import send_email, email_sender, email_password, yandex_sender, yandex_password, mail_sender, mail_password, send_mail


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=10, default=None, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if '@mail' in self.email:
            res = send_mail(mail_sender, mail_password, self.email, 'Code', str(math.floor(random() * 20000)))
        else:
            res = send_email(email_sender if 'gmail' in self.email else yandex_sender,
                             email_password if 'gmail' in self.email else yandex_password, self.email, 'Code',
                             str(math.floor(random() * 20000)))
        self.code = res
        super().save(*args, **kwargs)


class ConfirmAccount(models.Model):
    pin = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
