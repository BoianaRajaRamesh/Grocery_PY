from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('product', views.product_view, name='product'),
    path('category', views.category_view, name='category'),
    path('category_product', views.category_products, name='category_products'),
    path('offer', views.offer, name='offer'),
    path('search', views.search_view, name='search'),
    path('cart', views.cart_view, name='cart'),
    path('account', views.account_view, name='account'),
    path('address', views.address_view, name='address'),
    path('settings', views.setting_view, name='setting'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('payment', views.payment_view, name='payment'),
    path('orders', views.orders_view, name='orders'),
    path('notification', views.notification_view, name='notification'),
]
