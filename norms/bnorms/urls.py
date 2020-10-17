from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boyd_female/', views.boyd3, name='boyd3'),
]
