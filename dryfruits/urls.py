from django.urls import path 
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('',views.HomeView.as_view()),
    path('list/',views.DryfruitListView.as_view()),
]