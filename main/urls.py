from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name='gallery'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]