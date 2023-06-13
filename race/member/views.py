from .models import Member
from rest_framework.viewsets import ModelViewSet
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from .serializer import MemberSerializer, MemberCreateSerializer, MemberUpdateSerializer


class MemberViewSet(ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = MemberCreateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(MemberSerializer(instance).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MemberUpdateSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(MemberSerializer(instance).data, status=status.HTTP_200_OK)




