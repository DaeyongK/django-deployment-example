from django.urls import path
from authenticationApp import views

app_name = 'authenticationApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
