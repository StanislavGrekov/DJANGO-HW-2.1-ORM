import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        elements = []
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                elements.append({'id': (row['id']), 'name': row['name'],'image': row['image'], 'price': row['price'], 'release_date': row['release_date'], 'lte_exists': row['lte_exists']})

        for phone in elements:
            element = Phone(
                name = phone.get('name'),
                image = phone.get('image', None),
                price = phone.get('price'),
                release_date = phone.get('release_date'),
                lte_exists = phone.get('lte_exists'),
                slug='_'.join(phone.get('name').lower().split())
            )
            element.save()
