from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.all()
        categories.delete()

        category_list = [
            {'pk': '1', 'name': 'Рыба', 'description': ''},
            {'pk': '2', 'name': 'Говядина', 'description': ''},
            {'pk': '3', 'name': 'Птица', 'description': ''},
            {'pk': '4', 'name': 'Свинина', 'description': ''},
            {'pk': '5', 'name': 'Курица', 'description': ''}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        Category.objects.bulk_create(categories_for_create)