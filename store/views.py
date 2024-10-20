from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)

def login(request):
    context = {
        'page_title': 'Login'
    }
    return render(request, 'login.html', context)

def forgot_password(request):
    context = {
        'page_title': 'Forgot Password'
    }
    return render(request, 'forgot_password.html', context)

def register(request):
    context = {
        'page_title': 'Register'
    }
    return render(request, 'register.html', context)

def product_view(request):
    context = {
        'page_title': 'Product Details'
    }
    return render(request, 'product.html', context)

def category_view(request):
    context = {
        'page_title': 'Categories'
    }
    return render(request, 'category.html', context)

def category_products(request):
    context = {
        'page_title': 'Categories'
    }
    return render(request, 'category_products.html', context)

def search_view(request):
    context = {
        'page_title': 'Search'
    }
    return render(request, 'search.html', context)

def offer(request):
    context = {
        'page_title': 'Offers'
    }
    return render(request, 'offer.html', context)

def cart_view(request):
    context = {
        'page_title': 'Cart List'
    }
    return render(request, 'cart.html', context)

def account_view(request):
    context = {
        'page_title': 'Add Address'
    }
    return render(request, 'account.html', context)

def address_view(request):
   context = {
        'page_title': 'Add Address'
    }
   return render(request, 'address.html', context)


def setting_view(request):
   context = {
        'page_title': 'Profile Settings'
    }
   return render(request, 'setting.html', context)


def wishlist(request):
   context = {
        'page_title': 'Wishlist'
    }
   return render(request, 'wishlist.html', context)

def payment_view(request):
   context = {
        'page_title': 'Add Payment Method'
    }
   return render(request, 'payment.html', context)

def orders_view(request):
   context = {
        'page_title': 'Order History'
    }
   return render(request, 'orders.html', context)


def notification_view(request):
   context = {
        'page_title': 'Notification'
    }
   return render(request, 'notification.html', context)