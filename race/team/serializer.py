import uuid

from rest_framework import serializers
from .models import Team
from ..member.models import Member


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField(label='选手')

    class Meta:
        model = Team
        fields = (
            'id',
            'team_name',
            'team_group',
            'team_win',
            'team_lose',
            'team_desc',
            'members',
            'created_at',
            'updated_at'
        )

    def get_members(self, obj):
        mem_info = Team.objects.get(id=obj.id)
        member_list = []
        for m in mem_info.team.all():
            member_list.append({
                'name': m.member_name,
                'id': m.id
            })
        return member_list


class TeamCreateSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(allow_blank=True, allow_null=True)
    team_group = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Team
        fields = (
            'team_name',
            'team_group',
            'team_desc',
        )

    def validate_team_name(self, value):
        if not value:
            raise serializers.ValidationError(detail={
                'msg': '队名不能为空'
            })
        else:
            if Team.objects.filter(team_name=value):
                raise serializers.ValidationError(detail={
                    'msg': '队名已存在'
                })
        return value

    def create(self, validated_data):
        return super().create(validated_data)


class TeamUpdateSerializer(serializers.ModelSerializer):
    members = serializers.ListField(allow_empty=True)
    team_name = serializers.CharField()

    class Meta:
        model = Team
        fields = (
            'team_name',
            'team_group',
            'team_win',
            'team_lose',
            'team_desc',
            'members'
        )

    def validate_team_name(self, value):
        team = Team.objects.filter(team_name=value)
        if team:
            if team[0].id != self.instance.id:
                raise serializers.ValidationError(detail={
                    'msg': '该队名已存在'
                })
        return value

    def validate_members(self, value):
        ids = [x['id'] for x in value]
        if len(ids) > 8:
            raise serializers.ValidationError(detail={
                'msg': '成员不可超过8人'
            })
        if len(ids) != len(set(ids)):
            raise serializers.ValidationError(detail={
                'msg': '选手重复，请检查'
            })
        value_list = []
        for m in ids:
            member = Member.objects.filter(id=m)
            if not member:
                raise serializers.ValidationError(detail={
                    'msg': '请确定选手是否存在'
                })
            value_list.append(member[0])
        return value_list

    def update(self, instance, validated_data):
        team = Team.objects.get(id=instance.id)
        members = list(team.team.all())
        for member in validated_data['members']:
            if member.team_info_id and member.team_info_id != team.id:
                raise serializers.ValidationError(detail={
                    'msg': f'{member.member_name}选手已加入其他队伍'
                })

        remove_all = [member for member in members if member not in validated_data['members']]
        add_all = [member for member in validated_data['members'] if member not in members]

        for member in add_all:
            member.team_info_id = team.id
            member.save()

        for member in remove_all:
            member.team_info_id = None
            member.save()

        return super().update(instance, validated_data)
