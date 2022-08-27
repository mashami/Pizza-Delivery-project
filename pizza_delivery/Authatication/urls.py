import imp
from django.urls import path
from . import views
urlpatterns = [
    path('',views.HelloAuthAPIView.as_view()),
    path('signup/',views.UserAPIView.as_view(),name='Sign_up'),
    path ('register/', views.RegistrationUser.as_view(), name="register"),
    path ('Verify-Email/', views.VerifyEmail.as_view(), name="Verify-Email")
]
