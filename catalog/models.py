from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, **NULLABLE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    last_changes_date = models.DateTimeField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок', **NULLABLE)
    slug = models.CharField(max_length=100, verbose_name='ссылка', **NULLABLE)
    body = models.TextField(verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(verbose_name='опубликован', default=False)
    views_count = models.IntegerField(verbose_name='количество просмотров', **NULLABLE)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
