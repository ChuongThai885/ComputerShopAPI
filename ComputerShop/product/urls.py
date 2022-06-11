from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('getAllProduct/', views.getAllProductAPI.as_view(),name='getAllProduct'),
    path('getAllRadiator/',views.getAllRadiatorAPI.as_view(),name='getAllRadiator'),
    # path('getRadiator/<int:id>',views.getRadiatorAPI.as_view(),name='getRadiator'),
    path('getAllMainboard/', views.getAllMainboardAPI.as_view(),name='getAllMainboard'),
    path('getMainboard/<int:id>',views.getMainboardAPI.as_view(),name='getMainboard'),
]