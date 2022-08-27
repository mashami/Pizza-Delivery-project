
from rest_framework import serializers
from .models import Order


class OrdersCreateSerializer(serializers.ModelSerializer):
    Size=serializers.CharField(max_length=20)
    order_status=serializers.HiddenField(default='PENDIND')
    quantity=serializers.IntegerField()
    
    class Meta:
        model=Order
        fields=['id','Size','order_status','quantity']

class OrdersDetailSerializer(serializers.ModelSerializer):
    Size=serializers.CharField(max_length=20)
    order_status=serializers.CharField(default='PENDIND')
    quantity=serializers.IntegerField()
   
    created_at=serializers.DateTimeField()
    up_date_at=serializers.DateTimeField()
    class Meta:
        model=Order
        fields=['id','Size','order_status','quantity','created_at','up_date_at']
        
class UpdataOrderStatusSerializer(serializers.ModelSerializer):
    order_status=serializers.CharField(default='PENDIND')
    
    class Meta:
        model=Order
        fields=['order_status']