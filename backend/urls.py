from django.urls import path
from .views import *
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('videos/', VideoListAPIView.as_view(), name='video-list'),
]
