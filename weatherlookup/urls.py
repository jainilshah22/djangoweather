from django.urls import path

from weatherlookup import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
]