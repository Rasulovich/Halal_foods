
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Halal_foods.urls')),
    path('admin/', admin.site.urls),
]
