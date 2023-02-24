
from django.contrib import admin
from django.urls import path

# This is where the website URLs are defined

urlpatterns = [
    path("admin/", admin.site.urls),
]
