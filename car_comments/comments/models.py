from django.db import models
from datetime import datetime

class Country(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=False)

    def __str__(self) -> str:
        return self.name


class Producer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=False)
    country = models.ForeignKey('Country', verbose_name='Производитель', null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    name = models.CharField(verbose_name='Имя', null=False, max_length=128)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    year_start = models.PositiveSmallIntegerField(verbose_name='Начало выпуска', null=True, default=datetime.today().year)
    year_end = models.PositiveSmallIntegerField(verbose_name='Конец выпуска', null=True, default=datetime.today().year)

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    email = models.EmailField(verbose_name='email', null=False)
    car = models.ForeignKey('Car', verbose_name='Машина', null=False, on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='Комментарий', max_length=1024, null=False)
    create_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.email} - {self.car}'
    