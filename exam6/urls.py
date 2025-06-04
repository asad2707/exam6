
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from exam6 import settings
from exam6.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
]



if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)