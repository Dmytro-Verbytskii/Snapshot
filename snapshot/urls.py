from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('photogallery.urls', namespace="photogallery")),
    url(r'^auth/', include('users.urls', namespace="users")),
]
