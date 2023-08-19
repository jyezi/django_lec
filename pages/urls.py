from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('company/', views.company, name='company'),
    path('service/', views.service, name='service'),
    path('product/', views.product, name='product'),
    path('mysite/', views.card, name='card'),
    path('cs/', views.cs, name='cs'),
    path('greeting/', views.greeting, name='greeting'),
    path('history/', views.history, name='history'),

]
