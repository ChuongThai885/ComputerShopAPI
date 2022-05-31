from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
      path('getAllUser/',views.getAllUser.as_view(),name='getalluser'),
      path('register/',views.RegistrationAPI.as_view(),name="registration"),
]