from django.db import models
from accounts.models import Client
from accounts.utils import send_email, email_sender, email_password, yandex_sender, yandex_password


class Tare(models.Model):
    volume = models.FloatField()

    def __str__(self):
        return str(self.volume)

    class Meta:
        verbose_name = 'Тара'
        verbose_name_plural = 'Тары'


class Honey(models.Model):
    tare = models.IntegerField(verbose_name='Тара')
    title = models.CharField(max_length=255, verbose_name='Название мёда')
    description = models.TextField(verbose_name='Описания')
    date_of_purchase = models.DateTimeField(verbose_name='Дата покупки', auto_now_add=True)
    price = models.IntegerField(verbose_name='Цена')
    client = models.ForeignKey(Client, verbose_name='Покупатель', on_delete=models.CASCADE)
    images = models.ImageField(upload_to="photos/", verbose_name='Фото', null=True, blank=True)
    quantity = models.IntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.title} - {str(self.price)} - {str(self.tare.volume)}'

    class Meta:
        verbose_name = 'Мёд'
        verbose_name_plural = 'Мёд'


class Basket(models.Model):
    honey = models.ForeignKey(Honey, verbose_name='Мёд', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Покупатель', on_delete=models.CASCADE)

    def __str__(self):
        return self.honey.title

    def save(self, *args, **kwargs):
        honey = Honey.objects.get(id=self.honey.id)
        honey.quantity = honey.quantity + 1
        honey.save()
        super().save(*args, **kwargs)


class Feedback(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовог')
    text = models.TextField(verbose_name='Текс')
    client = models.ForeignKey(Client, verbose_name='Покупатель', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        send_email(email_sender if 'gmail' in self.client.email else yandex_sender,
        email_password if 'gmail' in self.client.email else yandex_password,
        self.client.email,
        self.title,
        self.text)
        super().save(*args, **kwargs)
