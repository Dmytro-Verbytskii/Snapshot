from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('photogallery.urls', namespace="photogallery")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^posts/', include('posts.urls', namespace="posts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
