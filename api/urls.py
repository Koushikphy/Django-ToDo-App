from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import routers



router = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')


urlpatterns = [
    url('api/', include(router.urls)),
    url(r'^$',views.index, name='home'),
    path('test/', views.getListofTodo, name='test'),
    path('test/<int:todo_id>', views.getSingleofTodo, name='test1'),
    path('testp/', views.putTodo, name='test2')
]


