from django.urls import path
from . import views

app_name = 'proteinWeb'
urlpatterns = [
    path('', views.index, name='home'),
]