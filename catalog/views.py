from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

    def get_queryset(self, **args):
        queryset = super().get_queryset(**args)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body', 'image', 'creation_date', 'is_published', 'views_count']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.slug = slugify(blog.title)
            blog.save()
        return super().form_valid(form)
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body', 'image', 'creation_date', 'is_published', 'views_count']
    success_url = reverse_lazy('list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list')