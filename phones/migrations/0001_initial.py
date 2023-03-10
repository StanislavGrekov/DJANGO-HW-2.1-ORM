# Generated by Django 4.1.5 on 2023-01-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название телефона')),
                ('image', models.URLField(verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('release_date', models.DateField(verbose_name='Дата')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug')),
            ],
        ),
    ]
