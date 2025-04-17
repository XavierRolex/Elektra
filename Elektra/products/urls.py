from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/<slug:slug>/', views.product_update, name='product_update'),
    path('delete/<slug:slug>/', views.product_delete, name='product_delete'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]