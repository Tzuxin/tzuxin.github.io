from django.urls import path, include
from .views import (
    UsersList,
    CreateUser,
    UserEmail,
    UpdateUser,
    DeleteUser,
)

app_name = 'polls'

urlpatterns = [
    path('', UsersList.as_view(), name='list'),
    path('create', CreateUser.as_view(), name='create'),
    path('<int:pk>/user', UserEmail.as_view(), name='user'),
    path('<int:pk>/update', UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete', DeleteUser.as_view(), name='delete'),
]