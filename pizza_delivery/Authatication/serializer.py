import email
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField




class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    phone_Number =PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(min_length=3,write_only=True)
    # confirm_password=serializers.CharField(min_length=3,write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','phone_Number','password']
        
        
    def validate(self, attrs):
        username_exits=User.objects.filter(username=attrs['username']).exists()
        if username_exits:
            raise ValidationErr(details="User name is already exists")
        
        email_exits=User.objects.filter(username=attrs['email']).exists()
        if email_exits:
            raise ValidationErr(details="email name is already exists ")
        
        phoneNumber_exits=User.objects.filter(username=attrs['phone_Number']).exists()
        if phoneNumber_exits:
            raise ValidationErr(details="phone_Number name is already exists")
        
        # if self.password != self.confirm_password | self.password is None:
        #     raise ValidationErr(details='Passwords must be the same ')
        
        return super().validate(attrs)
        
        
    
    
    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_Number=validated_data['phone_Number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=10, min_length=3, write_only=True)
    
    class Meta:
        model=User
        fields=['email','username','password']
        
    def validate(self, attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')
        if not username.isalnum():
            raise serializers.ValidationError('the user name should contain alphanumic characters')
        return attrs
    
    
    
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    