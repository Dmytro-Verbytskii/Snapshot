from __future__ import absolute_import
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^new_user', views.SignUpView.as_view(), name='signup'),
    url(r'^sign_in', views.LoginView.as_view(), name='login'),
    url(r'^sign_out', views.logout_view, name='logout')
]
