from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product, Blog


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'There is a message:{message} from {name}, with phone {phone}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body', 'image', 'creation_date', 'is_published', 'views_count']
    success_url = reverse_lazy('list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body', 'image', 'creation_date', 'is_published', 'views_count']
    success_url = reverse_lazy('list')