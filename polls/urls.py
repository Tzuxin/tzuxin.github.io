from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('login2', views.login2, name='login2'),
    path('signup', views.signup, name='signup'),
    path('delete_user', views.delete_user, name='delete_user')
]