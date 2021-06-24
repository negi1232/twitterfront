from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.views.generic import base
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    
    path('front/', include('front.urls')),
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)