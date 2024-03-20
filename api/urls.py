from django.urls import path
from . import views


urlpatterns = [
   # Category
   path('category-list/', views.category_list),
   path('category-create/', views.category_create),
   path('category-update/<int:id>/', views.category_update),
   path('category-detail/<int:id>/', views.category_detail),
   path('category-delete/<int:id>/', views.category_delete),
   # Product
   path('product-list/', views.products_list),
   path('product-create/', views.product_create),
   path('product-update/<int:id>/', views.product_update),
   path('product-detail/<int:id>/', views.product_detail),
   path('product-delete/<int:id>/', views.product_delete),
   # Cart
   path('cart-list/', views.cart_list),
   path('cart-create/', views.cart_create),
   path('cart-delete/<int:id>/', views.cart_delete),
   # Cart Product
   path('cart-product-list/', views.cart_product_list),
   path('cart-product-create/', views.cart_product_create),
   path('cart-product-detail/<int:id>/', views.cart_product_detail),
   path('cart-product-delete/<int:id>/', views.cart_product_delete),
   # Order
   path('order-list/', views.order_list),
   path('order-create/', views.order_create),
   path('order-update/<int:id>/', views.order_update),
   path('order-detail/<int:id>/', views.order_detail),
   path('order-delete/<int:id>/', views.order_delete),
   # Login - register
   path('login/', views.login),
   path('register/', views.register),
   path('logout/', views.logout),
]