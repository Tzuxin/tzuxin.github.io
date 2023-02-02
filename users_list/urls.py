from django.urls import path, include
from .views import UserAccountView

app_name = 'users_list'

url_patterns = [
    path('', UserAccountView.as_view(), name="user"),
]
