from django.urls import path

from catalog.views import contacts, ProductListView, ProductDetailView, BlogCreateView, BlogDetailView, BlogListView, \
    BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('list/', BlogListView.as_view(), name='list'),
]
