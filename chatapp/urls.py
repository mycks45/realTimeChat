from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name= 'room'),
    path('check_value', views.checkValue, name='check_value'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name= 'getMessages'),
]