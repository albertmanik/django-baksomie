
from django.contrib import admin
from django.urls import path , include

# BASE ROUTE
# http://127.0.0.1:8000/

urlpatterns = [ 
    path('', include('web.urls')), 
    path('login/', include('login.urls')),
    path('bakso/', include('bakso.urls')),
]
