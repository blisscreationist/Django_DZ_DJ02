from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company', views.company, name='company'),
    path('rast', views.rast, name='rast'),
    path('poly', views.poly, name='poly'),

]