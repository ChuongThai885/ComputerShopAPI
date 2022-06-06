from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = "user"

urlpatterns = [
      path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('getAllUser/',views.getAllUser.as_view(),name='getalluser'),
      path('register/',views.RegistrationAPI.as_view(),name="registration"),
      path('getuserinfor/',views.getUserInfor.as_view(),name="getuserinfor"),
]