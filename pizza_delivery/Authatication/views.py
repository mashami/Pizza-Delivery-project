from django.shortcuts import render
from rest_framework import generics,status, mixins
from rest_framework.response import Response
from .serializer import UserSerializer,RegistrationSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# Create your views here.

class HelloAuthAPIView(generics.GenericAPIView):
    def get(self,request):
        return Response({'message':'Auth successfully '},status=status.HTTP_200_OK)
    
    
class UserAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return self.list(request,status=status.HTTP_200_OK)
    
class RegistrationUser(generics.GenericAPIView):
    serializer_class=RegistrationSerializer
    def post(self, request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        user=User.objects.get(email=user_data['email'])
        token=RefreshToken.for_user(user).access_token
        
        current_site=get_current_site(request).domain
        relativeLink=reverse('Verify-Email')
        
        absurls='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='Hi' + user.username+'\n User this link below to verify your Email \n'+absurls
        data={'email_body':email_body, 'to_email': user.email,'Email_subject':'verify your email'}
        
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        pass
        