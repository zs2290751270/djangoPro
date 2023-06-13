from rest_framework import serializers

from ..models import *


class WsbSerializers(serializers.ModelSerializer):
    # extend = serializers.SerializerMethodField()

    class Meta:
        model = Wsb
        fields = '__all__'


class WsbCreateSerializers(serializers.ModelSerializer):

    content = serializers.CharField(allow_blank=True)

    class Meta:
        model = Wsb
        fields = '__all__'

    @staticmethod
    def validate_content(value):
        if Wsb.objects.filter(content=value):
            raise serializers.ValidationError(detail={
                'msg': 'content已存在'
            })
        if not value:
            value = 'blank'
        return value


class WsbUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Wsb
        fields = '__all__'

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
