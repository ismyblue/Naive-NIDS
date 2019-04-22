from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from nids.models import User
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
