from rest_framework.serializers import (
    ModelSerializer,
    # HyperlinkedIdentityField,
)
from django.contrib.auth.models import User

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'email',
        ]
