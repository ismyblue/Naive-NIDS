from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from nids.models import User, Role, FullEvent
import hashlib


########################################################################################################################
# 华丽的分割线，下面是返回相关界面的的函数 ############################################################################
############################################################################################    ############################
# def panel_index(request):
#     return redirect(reverse('nids:panel_login'))


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
            print(user.usr_name)
            request.session['usr_name'] = user.usr_name
            print('logined')
            return redirect(reverse('nids:panel_main'))
        else:
            return render(request, 'nids/login.html', {'error_message': '用户名不存在或密码错误！'})


def panel_main(request):
    """
    登录成功后的主界面
    :param request:
    :return:
    """
    return TemplateResponse(request, 'nids/index.html', {})


def panel_welcome(request):
    """
    返回欢迎界面（告警统计信息）
    :param request:
    :return:
    """
    return render(request, 'nids/welcome.html')


def panel_latest_warning(request, page_num):
    """
    最新告警界面
    :param request:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp')
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_latest_warning.html', {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num-1)})


def panel_event_detail(request, eid):
    """
    返回事件数据细节界面
    :param request:
    :param eid:
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


def panel_tcp_warning(request, page_num):
    """
    返回tcp告警界面
    :param request:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp').filter(ip_proto=6)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_tcp_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_udp_warning(request, page_num):
    """
    返回udp告警界面
    :param request:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp').filter(ip_proto=17)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_udp_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_icmp_warning(request, page_num):
    """
    返回icmp告警界面
    :param request:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp').filter(ip_proto=1)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_icmp_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_port_scan_warning(request, page_num):
    """
    返回端口扫描告警界面
    :param request:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp')
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_port_scan_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_srcip_warning(request, page_num):
    """
    返回源ip告警信息界面
    :param request:
    :return:
    """
    ip_srcs = FullEvent.objects.order_by('-timestamp').values('ip_src', 'ip_proto').distinct()
    iplist = set()
    for i in ip_srcs:
        iplist.add(i['ip_src'])
    ip_srcs = []
    for i in iplist:
        ip_srcs.append(FullEvent.objects.order_by('-timestamp').filter(ip_src=i)[0])
    p = Paginator(ip_srcs, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_srcip_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_srcip_list(request, ip_src, page_num):
    """
    返回某一源端口的所有告警列表中的某一页
    :param request:
    :param ip_src:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp').filter(ip_src=ip_src)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_srcip_list.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_dstip_warning(request, page_num):
    """
    返回目的ip告警信息界面
    :param request:
    :return:
    """
    ip_dsts = FullEvent.objects.order_by('-timestamp').values('ip_dst', 'ip_proto').distinct()
    iplist = set()
    for i in ip_dsts:
        iplist.add(i['ip_dst'])
    ip_dsts = []
    for i in iplist:
        ip_dsts.append(FullEvent.objects.order_by('-timestamp').filter(ip_dst=i)[0])
    p = Paginator(ip_dsts, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_dstip_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_dstip_list(request, ip_dst, page_num):
    """
    返回某一目标ip的所有告警列表中的某一页
    :param request:
    :param ip_dst:
    :param page_num:
    :return:
    """
    fullevents = FullEvent.objects.order_by('-timestamp').filter(ip_dst=ip_dst)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_dstip_list.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_srcport_warning(request, page_num):
    """
    返回源端口告警信息界面
    :param request:
    :return:
    """
    port_srcs = FullEvent.objects.order_by('-timestamp').values('port_src', 'ip_proto').distinct()
    portlist = set()
    for i in port_srcs:
        portlist.add(i['port_src'])
    port_srcs = []
    for i in portlist:
        port_srcs.append(FullEvent.objects.order_by('-timestamp').filter(port_src=i)[0])
    p = Paginator(port_srcs, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_srcport_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_srcport_list(request, port_src, page_num):
    """
    返回某一源端口的所有告警列表中的某一页
    :param request:
    :param port_src:
    :param page_num:
    :return:
    """
    if port_src == 'None':
        port_src = None
    fullevents = FullEvent.objects.order_by('-timestamp').filter(port_src=port_src)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_srcport_list.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_dstport_warning(request, page_num):
    """
    返回目的端口告警信息界面
    :param request:
    :return:
    """
    port_dsts = FullEvent.objects.order_by('-timestamp').values('port_dst', 'ip_proto').distinct()
    portlist = set()
    for i in port_dsts:
        portlist.add(i['port_dst'])
    port_dsts = []
    for i in portlist:
        port_dsts.append(FullEvent.objects.order_by('-timestamp').filter(port_dst=i)[0])
    p = Paginator(port_dsts, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_dstport_warning.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_dstport_list(request, port_dst, page_num):
    """
    返回某一目标端口的所有告警列表中的某一页
    :param request:
    :param ip_dst:
    :param page_num:
    :return:
    """
    if port_dst == 'None':
        port_dst = None
    fullevents = FullEvent.objects.order_by('-timestamp').filter(port_dst=port_dst)
    p = Paginator(fullevents, 25)
    page = p.get_page(page_num)
    return render(request, 'nids/panel_dstport_list.html',
                  {'warnings': page, 'page_total': p.num_pages, 'index': 25 * (page_num - 1)})


def panel_profile(request):
    """
    返回个人信息界面
    :param request:
    :return:
    """
    usr_id = int(request.session['usr_id'])
    user = User.objects.get(usr_id=usr_id)
    return TemplateResponse(request, 'nids/panel_profile.html', {'user': user})


def panel_profile_update(request):
    """
    返回个人信息修改界面
    :param request:
    :return:
    """
    if request.method == 'GET':
        usr_id = int(request.session['usr_id'])
        user = User.objects.get(usr_id=usr_id)
        return render(request, 'nids/panel_profile_update.html', {'user': user})
    elif request.method == 'POST':
        usr_id = request.session['usr_id']
        user = User.objects.get(usr_id=usr_id)
        usr_name = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        newpassword = request.POST.get('newpassword').strip()
        retrypassword = request.POST.get('retrypassword')
        if len(newpassword) > 0:
            if newpassword != retrypassword:
                message = '输入新密码不一致'
                return render(request, 'nids/panel_profile_update.html', {'user': user, 'error_message': message})
        password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()
        if password != user.usr_pwd:
            message = '原密码错误'
            return render(request, 'nids/panel_profile_update.html', {'user': user, 'error_message': message})
        user.usr_name = usr_name
        request.session['usr_name'] = usr_name
        if len(newpassword) > 0:
            user.usr_pwd = hashlib.md5(newpassword.encode('utf-8')).hexdigest()
        user.save()
        return render(request, 'nids/panel_profile_update.html', {'user': user, 'success_message': '修改成功'})


def panel_user_list(request, page_num):
    """
    返回用户列表界面,只有管理员才有权限访问
    :param request:
    :return:
    """
    usr_id = request.session['usr_id']
    users = User.objects.exclude(usr_id=usr_id)
    paginator = Paginator(users, 10)
    page = paginator.get_page(page_num)
    return render(request, 'nids/panel_user_list.html', {'users': page, 'page_total': paginator.num_pages})


def panel_user_update(request, usr_id):
    """
    用户更新界面 管理员可访问
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            user = User.objects.get(usr_id=usr_id)
            roles = Role.objects.all()
        except Exception as e:
            return render(request, 'nids/error.html', {'error_message': e})
        return render(request, 'nids/panel_user_update.html', {'user': user, 'roles': roles})
    elif request.method == 'POST':
        # try:
        print('post method')
        usr_login = request.POST.get('loginname').strip()
        usr_name = request.POST.get('username').strip()
        role_id = int(request.POST.get('role'))
        usr_enabled = bool(request.POST.get('status'))
        admin_pwd = request.POST.get('adminpassword').strip()
        admin_pwd = hashlib.md5(admin_pwd.encode('utf-8')).hexdigest()
        usr_pwd = request.POST.get('newpassword').strip()
        usr_retrypasswd = request.POST.get('retrypassword').strip()
        admin = User.objects.get(usr_id=request.session['usr_id'])
        user = User.objects.get(usr_id=usr_id)
        role = Role.objects.get(role_id=role_id)
        # 如果管理员密码错误，不允许修改用户信息
        if admin_pwd != admin.usr_pwd:
            return render(request, 'nids/panel_user_update.html', {'user': user, 'error_message': '管理员密码错误'})
        if len(usr_pwd) > 0 and usr_pwd == usr_retrypasswd:
            user.usr_pwd = hashlib.md5(usr_pwd.encode('utf-8')).hexdigest()
        user.usr_login = usr_login
        user.usr_name = usr_name
        user.role_id = role
        user.usr_enabled = usr_enabled
        try:
            user.save()
        except Exception as e:
            return render(request, 'nids/panel_user_update.html', {'user': user, 'error_message': e})
        else:
            return render(request, 'nids/panel_user_update.html', {'user': user, 'success_message': '修改成功'})
    else:
        return render(request, 'nids/error_message.html', {'error_message': '请求方法错误'})


def panel_user_create(request):
    """
    返回创建用户界面
    :param request:
    :return:
    """
    # GET请求，返回界面
    roles = Role.objects.all()
    if request.method == 'GET':
        return render(request, 'nids/panel_user_create.html', {'roles': roles})
    # POST请求，增加资源
    if request.method == 'POST':
        usr_login = request.POST.get('loginname')
        usr_name = request.POST.get('username')
        admin_pwd = request.POST.get('adminpassword')
        admin_pwd = hashlib.md5(admin_pwd.encode('utf-8')).hexdigest()
        usr_pwd = request.POST.get('password')
        retry_usr_pwd = request.POST.get('retrypassword')
        role_id = int(request.POST.get('role'))
        usr_enabled = request.POST.get('status')
        admin = User.objects.get(usr_id=int(request.session['usr_id']))
        if admin_pwd != admin.usr_pwd:
            return render(request, 'nids/panel_user_create.html', {'roles': roles, 'error_message': '管理员密码错误！'})
        # 密码不等不能创建账号
        if usr_pwd.strip() != retry_usr_pwd.strip():
            return render(request, 'nids/panel_user_create.html', {'roles': roles, 'error_message': '两次输入密码不相等！'})
        usr_pwd = hashlib.md5(usr_pwd.encode('utf-8')).hexdigest()
        role = Role.objects.get(role_id=role_id)
        user = User(usr_login=usr_login, usr_name=usr_name, usr_pwd=usr_pwd, role_id=role, usr_enabled=usr_enabled)
        try:
            user.save()
        except Exception as e:
            return render(request, 'nids/panel_user_create.html', {'roles': roles, 'error_message': e})
        return render(request, 'nids/panel_user_create.html', {'roles': roles, 'success_message': '创建用户成功！'})


def panel_role_list(request, page_num):
    """
    返回角色列表界面
    :param request:
    :return:
    """
    roles = Role.objects.all()
    paginator = Paginator(roles, 10)
    page = paginator.get_page(page_num)
    return render(request, 'nids/panel_role_list.html', {'roles': page, 'page_total': paginator.num_pages})


def panel_role_update(request, role_id):
    """
    返回角色更新界面或者处理角色更新请求
    :param request:
    :param role_id:
    :return:
    """
    # GET 请求返回界面
    if request.method == 'GET':
        role = Role.objects.get(role_id = int(role_id))
        return render(request, 'nids/panel_role_update.html', {'role': role})
    elif request.method == 'POST':
        role = Role.objects.get(role_id=role_id)
        admin = User.objects.get(usr_id=int(request.session['usr_id']))
        if admin.role_id.role_id != 1:
            return render(request, 'nids/error.html', {'error_message': '您没有权限更新角色信息！'})
        role_name = request.POST.get('rolename')
        role_desc = request.POST.get('roledesc')
        role.role_name = role_name
        role.role_desc = role_desc
        try:
            role.save()
        except Exception as e:
            return render(request, 'nids/panel_role_update.html', {'role': role, 'error_message': '更新失败' + e})
        else:
            return render(request, 'nids/panel_role_update.html', {'role': role, 'success_message': '更新成功'})


def panel_role_create(request):
    """
    返回创建角色界面，或者处理创建角色请求
    :param request:
    :return:
    """
    # GET请求，返回界面
    if request.method == 'GET':
        return render(request, 'nids/panel_role_create.html')
    # POST请求，增加角色资源
    if request.method == 'POST':
        role_name = request.POST.get('rolename')
        role_desc = request.POST.get('roledesc')
        admin_pwd = request.POST.get('adminpassword')
        admin_pwd = hashlib.md5(admin_pwd.encode('utf-8')).hexdigest()
        admin = User.objects.get(usr_id=int(request.session['usr_id']))
        if admin_pwd != admin.usr_pwd:
            return render(request, 'nids/panel_role_create.html', {'error_message': '管理员密码错误！'})
        # 密码不等不能创建账号
        role = Role(role_name=role_name, role_desc=role_desc)
        try:
            role.save()
        except Exception as e:
            return render(request, 'nids/panel_role_create.html', {'error_message': e})
        return render(request, 'nids/panel_role_create.html', {'success_message': '创建用户成功！'})


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


def __getip(ip):
    s = bin(int(ip))
    s = s[2:]
    s1 = s[0:8]
    s2 = s[8:16]
    s3 = s[16:24]
    s4 = s[24:32]
    return '{}.{}.{}.{}'.format(int(s1, 2), int(s2, 2), int(s3, 2), int(s4, 2))