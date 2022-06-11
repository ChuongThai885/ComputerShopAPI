from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
      path('getOrders/', views.getOrdersAPI.as_view(),name='getOrders'),
      path('getOrderDetail/<int:id_order>', views.getOrderDetailAPI.as_view(),name='getOrderDetail'),
]