from django.urls import path
from . import views

app_name = 'bakso'

urlpatterns = [
    path('bakso/', views.ListView.as_view(), name='index'),
    path('add-bakso/', views.CreateView, name='index'),
]
