import json

from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from hpcg_backend.review_search.modules.search import search_reviews


class ReviewSearchViewSet(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request)
        return Response([])

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        result_count = 3
        request_json = json.loads(request.body.decode("utf-8"))
        result = search_reviews(request_json['search'], n=result_count)

        return Response(result)
