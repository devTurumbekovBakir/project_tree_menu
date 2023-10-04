from django.urls import path, include

from menu import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nested/', views.nested_menu, name='nested_menu'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('multi-menu/', views.multi_menu, name='multi_menu'),
    path('category/<int:category_id>/', views.dynamic_url_menu, name='dynamic_url_menu'),
]
