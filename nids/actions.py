from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from nids.models import User, Role
import hashlib


########################################################################################################################
# 华丽的分割线，下面是执行相关动作的函数 ############################################################################
########################################################################################################################
def action_logout(request):
    '''
    注销账号，其实是删除session信息
    :param request:
    :return:
    '''
    print('注销前session',request.session.items())
    auth.logout(request)
    print('注销后session',request.session.items())
    return redirect(reverse('nids:panel_login'))


def action_user_delete(request, usr_id):
    '''
    删除某用户，只有管理员身份可以操作
    :param request:
    :param usr_id:
    :return:
    '''
    admin = User.objects.get(usr_id=int(request.session['usr_id']))
    if admin.role_id.role_id != 1:
        return render(request, 'nids/error.html', {'error_message': '您没有权限删除用户！'})
    user = User.objects.get(usr_id=usr_id)
    try:
        print(user)
        user.delete()
    except Exception as e:
        return render(request, 'nids/error.html', {'error_message': e})
    else:
        return HttpResponse('success')


def action_role_delete(request, role_id):
    """
    删除某角色，只有管理员身份可以操作
    :param request:
    :param role_id:
    :return:
    """
    admin = User.objects.get(usr_id=int(request.session['usr_id']))
    if admin.role_id.role_id != 1:
        return render(request, 'nids/error.html', {'error_message': '您没有权限删除角色！'})
    role = Role.objects.get(role_id=role_id)
    try:
        role.delete()
    except Exception as e:
        return render(request, 'nids/error.html', {'error_message': e})
    else:
        return HttpResponse('success')


def action_warning_delete(request, warning_id):
    pass