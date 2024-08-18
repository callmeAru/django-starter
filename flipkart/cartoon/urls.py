from django.urls import path
from .views import loginpg, homepage,register_view

urlpatterns = [
    path('register/',register_view, name='register'),
    path('', loginpg, name='loginpg'),
    path('home/', homepage, name='homepage'),
   
]
