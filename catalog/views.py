from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_product_categories


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

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['object'] = product_item
        context_data['title'] = f'{product_item.name}'
        return context_data

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

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
    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.slug = slugify(blog.title)
            blog.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('view_blog', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list')

class CategoryListView(ListView):
    model = Category

    extra_context = {
        'object_list': get_product_categories(),
        'title': 'Категории'
    }

