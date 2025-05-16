from django.urls import path
from .views import HomePageView, AboutPageView, ResumePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    path('html', ResumePageView.as_view(), name='html'),
    ]

