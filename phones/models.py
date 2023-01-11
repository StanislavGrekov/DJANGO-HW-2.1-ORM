from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название телефона')
    image = models.URLField(verbose_name='Изображение')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=100, blank=True,unique=True,verbose_name='slug')


