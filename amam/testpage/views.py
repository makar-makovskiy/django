from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ResumePageView(TemplateView):
        template_name = 'html.html'

# def index(request):
#     return HttpResponse("Salamalekum bratva")
# def hello(request):
#     return HttpResponse("IYJMNIOYIOUHPJOUJHPO")
# # Create your views here.
