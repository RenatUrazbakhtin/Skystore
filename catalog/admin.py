from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


# Register your models here.
# admin.site.register(Student)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'active_version')