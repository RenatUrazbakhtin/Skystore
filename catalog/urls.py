from django.urls import path

from catalog.views import contacts, ProductListView, ProductDetailView, BlogCreateView, BlogDetailView, BlogListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    #path('update/',..., name='update'),
    #path('delete/',..., name='delete')
    path('list/', BlogListView.as_view(), name='list'),
]
