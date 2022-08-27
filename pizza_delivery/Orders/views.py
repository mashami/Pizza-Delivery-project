from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Order
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

# class HelloOrderAPIView(generics.GenericAPIView):
#     def get(self,request):
#         return Response({'message':'Order successfully '},status=status.HTTP_200_OK)
    
    
class OrderCreateListAPIView(generics.GenericAPIView):
    serializer_classes=OrdersCreateSerializer
    queryset=Order.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[IsAdminUser]
    def get(self,request):
        orders=Order.objects.all()
        serializer=self.serializer_classes(instance=orders,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_classes(data=data)
        user=request.user
        
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
class OrderDetailsAPIView(generics.GenericAPIView):
    serializer_classes=OrdersDetailSerializer
    permission_classes=[IsAdminUser]
    def get(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_classes(instance=order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        data=request.data
        serializer=self.serializer_classes(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def delete(self,requesr,order_id):
        order=get_object_or_404(Order, pk=order_id)
        
        order.delete()
        return Response(status=status.HTTP_200_OK)
    

class UpdataOrderStatusAPIView(generics.GenericAPIView):
    serializer_classes=UpdataOrderStatusSerializer
    permission_classes=[IsAdminUser]
    def put(self,request,order_id):
        order=get_object_or_404(Order, pk=order_id)
        
        data=request.data
        serializer=self.serializer_classes(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserOrderAPIView(generics.GenericAPIView):
    serializer_class=OrdersDetailSerializer
    
    def get(self,request,user_id):
        data=request.data
        
        user=User.objects.get(pk=user_id)
        orders=Order.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetailsAPIView(generics.GenericAPIView):
    serializer_class=OrdersDetailSerializer
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        
        order=Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer=self.serializer_class(instance=order)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)