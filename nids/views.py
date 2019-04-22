from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from nids.models import User
import hashlib


########################################################################################################################
# 华丽的分割线，下面是返回相关界面的的函数 ############################################################################
########################################################################################################################
def panel_index(request):
    return redirect(reverse('nids:panel_login'))


def panel_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'nids/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        # user = get_object_or_404(User, usr_login=username)
        try:
            user = User.objects.get(usr_login=username)
        except User.DoesNotExist:
            return render(request, 'nids/login.html', {'error_message': '用户名不存在或密码错误！'})
        password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()
        if password == user.usr_pwd:
            request.session['login_status'] = True
            request.session['usr_id'] = user.usr_id
            return redirect(reverse('nids:panel_main'))
        else:
            return render(request, 'nids/login.html', {'error_message': '用户名不存在或密码错误！'})


def panel_main(request):
    """
    登录成功后的主界面
    :param request:
    :return:
    """
    return render(request, 'nids/index.html')


def panel_welcome(request):
    """
    返回欢迎界面（告警统计信息）
    :param request:
    :return:
    """
    return render(request, 'nids/welcome.html')


def panel_latest_warning(request):
    """
    最新告警界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_log_query(request):
    """
    返回日志查询界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_log_export_history(request):
    """
    返回日志导出记录界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_tcp_warning(request):
    """
    返回tcp告警界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_udp_warning(request):
    """
    返回udp告警界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_icmp_warning(request):
    """
    返回icmp告警界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_port_scan_warning(request):
    """
    返回端口扫描告警界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_srcip_warning(request):
    """
    返回源ip告警信息界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_dstip_warning(request):
    """
    返回目的ip告警信息界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_srcport_warning(request):
    """
    返回源端口告警信息界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_dstport_warning(request):
    """
    返回目的端口告警信息界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_profile(request):
    """
    返回个人信息界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_profile_update(request):
    """
    返回个人信息修改界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_user_list(request):
    """
    返回用户列表界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_user_create(request):
    """
    返回创建用户界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_role_list(request):
    """
    返回角色列表界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_role_create(request):
    """
    返回角色创建界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_setting(request):
    """
    返回系统设置界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_system_log(request):
    """
    返回系统日志界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_shutdown_reboot(request):
    """
    返回系统重启关闭界面
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')


def panel_event_detail(request):
    """
    时间细节
    :param request:
    :return:
    """
    return HttpResponse('Hello World!')





