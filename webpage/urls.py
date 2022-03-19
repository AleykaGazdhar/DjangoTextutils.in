from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('analyze.html', views.analyze, name="analyze"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('nooperation.html', views.nooperation, name="nooperation")   
]





