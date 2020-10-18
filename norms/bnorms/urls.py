from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boyd_female/', views.boyd3, name='boyd3'),
    re_path(r'^boyd_female/(?P<value>\d+\.\d{2})/$', views.boyd3onegirl, name='boyd3onegirl'),
]
