

from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics

from .serializers import PlayerSerializer, TeamSerializer
from .pagination import BasePagination, TeamPagination


from .models import Team, Player
from typing import List







class PlayersView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    pagination_class = BasePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    def get_queryset(self):
        order = self.request.query_params.get('order')
        queryset = Player.objects.all().order_by( '-name' if order == 'desc' else 'name')
        return queryset


class TeamView(generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = TeamPagination
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name',]

    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        name = request.data.get('Name','')
        if name:
            name = name.title()

        queryset = self.queryset.filter(name__startswith=name)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

