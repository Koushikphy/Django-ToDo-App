from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import routers



router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')



urlpatterns = [
    # home page route
    url(r'^$',views.index, name='home'),

    # route todo query api
    url('api/', include(router.urls)),

    # user registration api route
    path('register/', views.RegisterUserView.as_view()),

    # user login api route
    path('login/', views.LoginUserView.as_view()),

    # user logout api route
    path('logout/', views.logOutUser),


]


