from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import routers



router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')
# router1.register('users', views.UserViewSets, basename='users')



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

    # user
    # url('apis/', include(router1.urls)),
    # url('user/',views.userView, name='user'),
    # path('test/', views.registerUser, name='test'),
    # path('test/<int:todo_id>', views.getSingleofTodo, name='test1'),
    # path('testp/', views.putTodo, name='test2'),
    # url('ind/', views.test, name='file')
]


