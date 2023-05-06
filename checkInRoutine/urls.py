from django.urls import path

from . import views

urlpatterns = [
    path('',views.step1, name='index')
]
