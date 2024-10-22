from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

STATUS_BOOLEN = (
    (0, 0),  # Active
    (1, 1),  # Inactive
)


class User(AbstractUser):
    mobile = models.CharField(max_length=15, db_index=True, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, db_index=True, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(db_column='status', choices=STATUS_BOOLEN, default=1)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', default=timezone.now)

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    userId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, unique=True, blank=True, null=True)
    city = models.CharField(max_length=100, unique=True, blank=True, null=True)
    pincode = models.CharField(max_length=10, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, unique=True, blank=True, null=True)
    latitude = models.CharField(max_length=25, unique=True, blank=True, null=True)
    longitude = models.CharField(max_length=25, unique=True, blank=True, null=True)
    status = models.SmallIntegerField(db_column='status', choices=STATUS_BOOLEN, default=1)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', default=timezone.now)

    def __str__(self):
        return self.name


class Categories(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    parentId = models.ForeignKey('self', db_column='parent_id', db_index=True, null=True, on_delete=models.SET_NULL,
                                 blank=True)
    category = models.CharField(db_column='category', max_length=1000, null=True)
    code = models.CharField(db_column='code', max_length=100, null=True)
    path = models.CharField(db_column='path', max_length=250, null=True, blank=True)
    level = models.IntegerField(db_column='level', default=0)
    childrenCount = models.IntegerField(db_column='children_count', default=0)
    mediaPaths = models.CharField(db_column='media_paths', max_length=250, null=True, blank=True)
    status = models.SmallIntegerField(db_column='status', choices=STATUS_BOOLEN, default=1)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', default=timezone.now)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category


class Products(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    parentId = models.ForeignKey('self', db_column='parent_id', db_index=True, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(db_column='sku', max_length=255, null=True, blank=True)
    productName = models.CharField(db_column='product_name', db_index=True, max_length=255, null=True, blank=True)
    categoryId = models.ManyToManyField(Categories, db_column='category_ids', db_index=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    images = models.JSONField(db_column='images', max_length=255, null=True, blank=True)
    stock = models.IntegerField(db_column='stock', null=True, blank=True)
    price = models.CharField(db_column='price', max_length=25, null=True, blank=True)
    minSaleQty = models.IntegerField(db_column='min_sal_qty', null=True, blank=True, default=1)
    attributes = models.JSONField(db_column='attributes', null=True, blank=True)
    status = models.SmallIntegerField(db_column='status', choices=STATUS_BOOLEN, default=1)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', default=timezone.now)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.productName


class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    code = models.CharField(max_length=50, db_column='code', unique=True, null=True, blank=True)
    orderStatus = models.CharField(max_length=150, db_column='status', null=True, blank=True)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return self.code


class Orders(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    orderNumber = models.CharField(max_length=50, unique=True, db_column='po_number', null=True, blank=True)
    userId = models.ForeignKey(User, db_column='user_id', null=True, on_delete=models.SET_NULL)
    shippingAddress = models.ForeignKey(Address, db_column='shipping_address', related_name='po_shipping_address',
                                        null=True, on_delete=models.SET_NULL)
    billingAddress = models.ForeignKey(Address, db_column='billing_address', related_name='po_billing_address',
                                       null=True, on_delete=models.SET_NULL)
    PoCreatedDate = models.DateField(db_column='po_created_date', null=True, blank=True)
    paymentMode = models.CharField(max_length=50, db_column='payment_mode', null=True, blank=True)
    cancelReason = models.CharField(max_length=1000, db_column='cancel_reason', null=True, blank=True)
    totalQty = models.IntegerField(db_column='total_qty', default=0, null=True, blank=True)
    totalAmount = models.FloatField(db_column='total_amount', default=0, null=True, blank=True)
    status = models.ForeignKey(OrderStatus, db_column='status', null=True, on_delete=models.SET_NULL)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        db_table = 'order_details'

    def __str__(self):
        return self.orderNumber


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, db_column='id')
    orderId = models.ForeignKey(Orders, db_column='po_id', null=True, on_delete=models.SET_NULL)
    productId = models.ForeignKey(Products, db_column='product_id', null=True, on_delete=models.SET_NULL)
    qty = models.IntegerField(db_column='qty', default=0, null=True, blank=True)
    unitPrice = models.FloatField(db_column='unit_price', default=0, null=True, blank=True)
    gstPercentage = models.FloatField(db_column='gst_percentage', default=0, null=True, blank=True)
    gst = models.FloatField(db_column='gst', default=0, null=True, blank=True)
    discountPercentage = models.FloatField(db_column='discount_percentage', default=0, null=True, blank=True)
    discount = models.FloatField(db_column='discount', default=0, null=True, blank=True)
    insurance = models.FloatField(db_column='insurance', default=0, null=True, blank=True)
    logistics = models.FloatField(db_column='logistics', default=0, null=True, blank=True)
    shipping = models.FloatField(db_column='shipping', default=0, null=True, blank=True)
    totalAmount = models.FloatField(db_column='total_amount', default=0, null=True, blank=True)
    info = models.TextField(db_column='info', null=True, blank=True)
    status = models.SmallIntegerField(db_column='status', choices=STATUS_BOOLEN, default=1)
    createdDate = models.DateTimeField(db_column='created_date', default=timezone.now)
    updatedDate = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        db_table = 'order_items'

    def __int__(self):
        return self.id
