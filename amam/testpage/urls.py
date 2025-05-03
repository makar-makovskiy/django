from django.urls import path
from .views import index
from .views import hello

urlpatterns = [
    path('', index, name='index'),
    path('opop/', hello, name='hello'),
    ]

