from functools import partial

from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):
    @extend_schema(exclude=True)
    def get(self, request, format=None):
        get_url = partial(reverse, request=request, format=format)

        return Response({
            # 'docs': get_url('api:docs'),
            'polls': get_url('api:polls:list'),
            # 'users_list': get_url('api:users_list:list'),
        })