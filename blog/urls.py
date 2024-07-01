# blog/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # Ensure this line correctly references your app's URLs
]
