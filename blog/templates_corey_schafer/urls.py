from django.urls import path
from . import views
from .views import PostDetailView

app_name = 'corey_schafer'

urlpatterns = [
    path('', views.home, name='templates-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='templates-about'),
]

