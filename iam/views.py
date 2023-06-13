import json
from django.http import JsonResponse
from django.contrib.auth.models import User, Permission, PermissionsMixin
from rest_framework import permissions
from rest_framework.generics import ListAPIView


class Iam(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    # 添加用户
    @staticmethod
    def post(request):
        json_dict = json.loads(request.body)
        username = json_dict['username']
        password = json_dict['password']
        try:
            User.objects.get(username=username)
            return JsonResponse({'msg': u'用户已存在'},
                                content_type="application/json,charset=utf-8",
                                json_dumps_params={'ensure_ascii': False})
        except User.DoesNotExist:
            User.objects.create_user(username=username, password=password)
            user_info = {
                'username': username,
                'password': password,
                'is_staff': True
            }
            return JsonResponse({'msg': 'success', 'data': user_info})

    # 修改用户信息
    @staticmethod
    def put(request):
        json_dict = json.loads(request.body)
        username = json_dict['username']
        password = json_dict['password']
        try:

            user_obj = User.objects.get(username=username)
            user_obj.set_password(password)
            user_obj.save()
            data = {
                'username': username,
                'password': password
            }
            return JsonResponse(
                {'msg': 'success', 'data': data},
                content_type="application/json,charset=utf-8",
                json_dumps_params={'ensure_ascii': False}
            )
        except User.DoseNotExist:
            return JsonResponse({'msg': u'用户不存在'},
                                content_type="application/json,charset=utf-8",
                                json_dumps_params={'ensure_ascii': False})

    # 查看用户列表
    @staticmethod
    def get(request, pk=None):
        if not pk:
            user_info = list(User.objects.all().values())
            data = []
            for i in user_info:
                data.append({
                    'id': dict(i)['id'],
                    'username': dict(i)['username'],
                })
            return JsonResponse(
                {'data': data},
                content_type="application/json,charset=utf-8",
            )
        else:
            Iam.get_user_detail(request, pk)

    # 删除用户
    @staticmethod
    def delete(request, pk):
        try:
            user = User.objects.get(username=pk)
            if user.is_superuser:
                return JsonResponse(
                    {'msg': '超级用户不可删除'},
                    json_dumps_params={'ensure_ascii': False},
                    status=200
                )
            user.delete()
            return JsonResponse(
                {'msg': '删除用户成功'},
                status=204
            )
        except User.DoesNotExist:
            return JsonResponse(
                {'msg': '用户不存在'},
                json_dumps_params={'ensure_ascii': False},
                status=404
            )


class IamDetail(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # 查看用户详情

    @staticmethod
    def get(request, pk):
        user_detail = User.objects.get(username=pk)
        data = {
            'username': user_detail.username,
            'add_time': user_detail.date_joined
        }
        return JsonResponse(
            {'data': data},
            content_type="application/json,charset=utf-8"
        )


class PermissionM(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, pk):
        user = User.objects.get(username=pk)
        all_per = list(user.get_user_permissions())
        perm_res = {'permission': all_per}
        return JsonResponse(
            perm_res,
            content_type="application/json,charset=utf-8"
        )

    @staticmethod
    def post(request, pk):
        json_dict = json.loads(request.body)
        print(json_dict)
        user = User.objects.get(username=pk)
        perm1 = Permission.objects.get(codename='delete_user')
        user.user_permissions.add(perm1)
        return JsonResponse(
            {'msg': 'add permission success'},
            content_type="application/json,charset=utf-8"
        )






