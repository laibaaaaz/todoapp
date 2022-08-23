from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name = 'index'),
    path('delete/<int:i>', views.delete, name='delete'),
    path('', views.loginview, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutview, name='logout')    
]
