from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    team_id = serializers.SerializerMethodField(label='队伍ID')
    team_name = serializers.SerializerMethodField(label='队伍名称')

    class Meta:
        model = Member
        fields = ('id', 'member_name', 'member_code', 'member_desc', 'is_leader', 'team_id', 'team_name', 'created_at',
                  'updated_at')

    def get_team_id(self, obj):
        if getattr(obj.team_info, 'id', None):
            return obj.team_info.id
        return ''

    def get_team_name(self, obj):
        if getattr(obj.team_info, 'team_name', None):
            return obj.team_info.team_name
        return ''


class MemberCreateSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(allow_blank=True, allow_null=True, required=True)
    member_code = serializers.CharField(allow_blank=True, allow_null=True, required=True)

    class Meta:
        model = Member
        fields = ('id', 'member_name', 'member_code', 'member_desc', 'is_leader', 'team_info')

    @staticmethod
    def validate_member_name(value):
        if not value:
            raise serializers.ValidationError(detail={
                'detail': {
                    'msg': '选手名字不可为空',
                },
            })
        else:
            if Member.objects.filter(member_name=value):
                raise serializers.ValidationError(detail={
                    'detail': {
                        'msg': '该选手名已存在',
                    },
                })
        return value

    @staticmethod
    def validate_member_code(value):
        if not value:
            raise serializers.ValidationError(detail={
                'detail': {
                    'msg': '选手工号不可为空',
                },
            })
        else:
            if Member.objects.filter(member_code=value):
                raise serializers.ValidationError(detail={
                    'detail': {
                        'msg': '该选手工号已存在',
                    },
                })
        return value

    def create(self, validated_data):
        return super().create(validated_data)


class MemberUpdateSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(allow_blank=True, allow_null=True, required=True)
    member_code = serializers.CharField(allow_blank=True, allow_null=True, required=True)

    class Meta:
        model = Member
        fields = ('member_name', 'member_code', 'member_desc')

    @staticmethod
    def validate_member_name(value):
        if not value:
            raise serializers.ValidationError(detail={
                'detail': {
                    'msg': '选手名字不可为空',
                },
            })
        else:
            if Member.objects.filter(member_name=value):
                raise serializers.ValidationError(detail={
                    'detail': {
                        'msg': '该选手名已存在',
                    },
                })
        return value

    @staticmethod
    def validate_member_code(value):
        if not value:
            raise serializers.ValidationError(detail={
                'detail': {
                    'msg': '选手工号不可为空',
                },
            })
        else:
            if Member.objects.filter(member_code=value):
                raise serializers.ValidationError(detail={
                    'detail': {
                        'msg': '该选手工号已存在',
                    },
                })
        return value

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
