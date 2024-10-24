from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('make-appointment/', views.make_appointment, name='make_appointment'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
]
