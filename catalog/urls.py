from django.urls import path

from catalog.views import home, contacts, product



urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product, name='product'),
]
