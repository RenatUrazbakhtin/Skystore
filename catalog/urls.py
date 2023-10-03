from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts, ProductListView, ProductDetailView, BlogCreateView, BlogDetailView, BlogListView, \
    BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('list/', BlogListView.as_view(), name='list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]
