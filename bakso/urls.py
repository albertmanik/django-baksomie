from django.urls import path
from . import views

app_name = 'bakso'

urlpatterns = [
    path('bakso/', views.index, name='index'),
]
