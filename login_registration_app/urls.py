from django.urls import path
from rest_framework.urls import urlpatterns
from login_registration_app import views

urlpatterns = [
    path('', views.index, name='accounts'),
    path('signup/', views.signup, name='signup')
]