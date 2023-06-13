from .models import *
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import WsbSerializers, WsbCreateSerializers, WsbUpdateSerializers


class WsbView(ModelViewSet):

    queryset = Wsb.objects.all()
    serializer_class = WsbSerializers
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializers = WsbCreateSerializers(
            data=request.data
        )
        serializers.is_valid(raise_exception=True)
        instance = serializers.save()
        return Response(WsbSerializers(instance).data, status=201)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = WsbUpdateSerializers(
            instance,
            data=request.data,
            partial=True,
        )
        serializers.is_valid(raise_exception=True)
        instance = serializers.save()
        return Response(WsbSerializers(instance).data, status=200)

