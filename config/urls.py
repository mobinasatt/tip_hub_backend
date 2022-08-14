from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Third party apps
    path('accounts/', include('allauth.urls')),
    # Local urls
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('home.urls', namespace='home')),
]
