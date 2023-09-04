from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'There is a message:{message} from {name}, with phone {phone}')
    return render(request, 'catalog/contacts.html')

def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': f'Товар - {Product.name}',
    }
    return render(request, 'catalog/product.html', context)