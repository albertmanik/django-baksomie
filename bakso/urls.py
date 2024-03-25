from django.urls import path
from . import views

app_name = 'bakso'

urlpatterns = [
    path('', views.BaksoView.as_view(), name='list'),
    path('add-bakso/', views.CreateView.as_view(), name='add'),
    path('delete-bakso/<int:pk>', views.DeleteBaksoView.as_view(), name='delete'),
]
