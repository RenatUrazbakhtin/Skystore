from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

class Product(models.Model):
    def __str__(self):
        pass

class Category(models.Model):
    def __str__(self):
        pass