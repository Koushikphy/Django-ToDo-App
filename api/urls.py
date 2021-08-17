from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers



router = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')


urlpatterns = [
    url('api/', include(router.urls)),
    url("",views.index, name='home'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)