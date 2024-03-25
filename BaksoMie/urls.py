
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

# BASE ROUTE
# http://127.0.0.1:8000/

urlpatterns = [ 
    path('', include('web.urls')), 
    path('login/', include('login.urls')),
    path('dashboard/bakso/', include('bakso.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
