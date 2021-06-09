from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('lavash/', lavash, name='lavash'),
    path('ichmliklar/', ichmliklar, name='ichmliklar'),
    path('salatlar/', salatlar, name='salatlar'),
    path('ovqatlar/', ovqatlar, name='ovqatlar'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
