from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('elektrastore.urls')),
] + static(settings.MEDIA_URL, documentation_root=settings.MEDIA_ROOT)
