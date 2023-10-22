
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import frontpage, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('', frontpage, name='frontpage'),
    path('verification/', include('verify_email.urls')),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
