from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
