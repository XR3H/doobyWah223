from django.urls import path, include, re_path

from drf_auth.views import *

urlpatterns = [
    path('', index),
    path('t_auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]