from django.db import models


class Country(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=True, default='неизвестно')


class Producer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, default='неизвестно')
    producer = models.ForeignKey(to=Country, verbose_name='Производитель', on_delete=models.SET_DEFAULT)


class Car(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128)
    producer = models.ForeignKey(to=Producer, on_delete=models.SET_DEFAULT, default='неизвестно')
    year_start = models.DateField(verbose_name='Начало производства', null=False)
