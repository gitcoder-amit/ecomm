from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Dryfruit

class HomeView(TemplateView):
    template_name='home.html'


class DryfruitListView(ListView):
    model=Dryfruit
