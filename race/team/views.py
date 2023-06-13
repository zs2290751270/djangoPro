from .models import Team
from rest_framework.viewsets import ModelViewSet
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializer import TeamSerializer, TeamCreateSerializer, TeamUpdateSerializer


class TeamViewSet(ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = TeamCreateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(TeamSerializer(instance).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TeamUpdateSerializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(TeamSerializer(instance).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='test')
    def get_info(self, request, *args, **kwargs):
        return Response([1, 2, 3, 4], status=200)
