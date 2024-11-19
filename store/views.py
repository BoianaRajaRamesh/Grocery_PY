from django.shortcuts import render
from .models import  *
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    categories = Categories.objects.filter(status=1, parentId__isnull=True).order_by('?').all()[:8]
    context = {
        'page_title': 'Home',
        'categories': categories
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

def category_view(request, category_id=""):
    parent_categories = Categories.objects.filter(status=1, parentId__isnull=True)
    categories = Categories.objects.filter(status=1)
    if category_id != "":
        categories = categories.filter(parentId=category_id).all()
    else:
        category_id = 1
        categories = categories.filter(parentId=1).all()
    context = {
        'page_title': 'Categories',
        'categories': parent_categories,
        'sub_categories': categories,
        'category_id': category_id
    }
    return render(request, 'category.html', context)

def category_products(request, category_id = ""):
    if category_id == "":
        category_id = 1
    category = Categories.objects.filter(status=1, id=category_id).get()
    all_sub_categories = Categories.objects.filter(status=1, parentId=category.parentId).all()
    context = {
        'page_title': 'Categories',
        'category': category,
        'sub_categories': all_sub_categories
    }
    return render(request, 'category_products.html', context)

def category_content(request, category_id):
    # parent_categories = Categories.objects.filter(status=1, parentId__isnull=True)
    categories = Categories.objects.filter(status=1)
    if category_id != "":
        categories = categories.filter(parentId=category_id).all()
    else:
        category_id = 1
        categories = categories.filter(parentId=1).all()

    # Render the subcategories as HTML
    sub_categories_html = render_to_string('partials/_sub_categories.html', {'sub_categories': categories})

    return JsonResponse({
        'sub_categories_html': sub_categories_html
    })

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

def order_details_view(request):
   context = {
        'page_title': 'Order Summary'
    }
   return render(request, 'order-detail.html', context)