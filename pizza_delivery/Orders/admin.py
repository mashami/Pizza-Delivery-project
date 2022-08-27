from django.contrib import admin
from .models import Order
# Register your models here.
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','Size','order_status','quantity','created_at']
    list_filter=['created_at','Size','order_status']