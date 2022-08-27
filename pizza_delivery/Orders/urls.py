
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.OrderCreateListAPIView.as_view(),name='order'),
    path('<int:order_id>/',views.OrderDetailsAPIView.as_view(),name='order_details'),
    path('update_status/<int:order_id>/',views.UpdataOrderStatusAPIView.as_view(),name='updateStatusOrder'),
    path('user/<int:user_id>/',views.UserOrderAPIView.as_view(),name='user_orders'),
    path('user/<int:user_id>/order/<int:order_id>',views.UserOrderDetailsAPIView.as_view(),name='user_spefic_details')
    
]
