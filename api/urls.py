from django.urls import path, include

from .views import APIRoot

app_name = 'api'

urlpatterns = [
    path('', APIRoot.as_view(), name='root'),
    path('polls/', include('polls.api.urls'), name='polls'),
    # path('users_list/', include('users_list.api.urls'), name='users_list'),
]