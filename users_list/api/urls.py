from django.urls import path, include
from .views import UserAccount

app_name = 'users_list'

url_patterns = [
    path('', UserAccount.as_view(), name="list"),
]
