from django.contrib import admin
from .models import User, Address, Categories, Products, OrderStatus, Orders, OrderItems


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'email', 'dob', 'status', 'createdDate', 'updatedDate')
    search_fields = ('username', 'email', 'mobile')
    list_filter = ('status',)
    ordering = ('-createdDate',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('userId', 'mobile', 'name', 'state', 'city', 'pincode', 'status', 'createdDate', 'updatedDate')
    search_fields = ('mobile', 'state', 'city', 'pincode')
    list_filter = ('status',)
    ordering = ('-createdDate',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category', 'parentId', 'level', 'childrenCount', 'status', 'createdDate', 'updatedDate')
    search_fields = ('category', 'code')
    list_filter = ('status',)
    ordering = ('-createdDate',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('productName', 'get_categoryId', 'stock', 'price', 'minSaleQty', 'status', 'createdDate', 'updatedDate')
    search_fields = ('productName', 'sku')
    list_filter = ('status', 'categoryId')
    ordering = ('-createdDate',)

    def get_categoryId(self, obj):
        return ", ".join([category.category for category in obj.Categories.all()])

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'orderStatus', 'createdDate', 'updatedDate')
    search_fields = ('code', 'orderStatus')
    ordering = ('-createdDate',)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('orderNumber', 'userId', 'shippingAddress', 'billingAddress', 'totalQty', 'totalAmount', 'status', 'createdDate', 'updatedDate')
    search_fields = ('orderNumber', 'userId__username', 'shippingAddress__name', 'billingAddress__name')
    list_filter = ('status',)
    ordering = ('-createdDate',)


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'productId', 'qty', 'unitPrice', 'totalAmount', 'status', 'createdDate', 'updatedDate')
    search_fields = ('orderId__orderNumber', 'productId__productName')
    list_filter = ('status',)
    ordering = ('-createdDate',)
