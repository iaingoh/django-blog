from django.urls import path
from . import views

app_name = 'user_registration'

urlpatterns = [
    path('', views.UserFormView.as_view(), name='register')
    ]