from django.urls import path
from nids import views, actions


app_name = 'nids'
urlpatterns = [
    # 首页界面url
    path('', views.panel_index, name='index'),
    # 登录界面url，包括登录动作
    path('panel_login/', views.panel_login, name='panel_login'),
    # 控制台主界面
    path('panel_main/', views.panel_main, name='panel_main'),
    # 欢迎界面，告警信息统计界面
    path('panel_welcome/', views.panel_welcome, name='panel_welcome'),
    # 最新告警界面
    path('panel_latest_warning/', views.panel_latest_warning, name='panel_latest_warning'),
    # 日志查询界面
    path('panel_log_query/', views.panel_log_query, name='panel_log_query'),
    # 日志导出记录界面
    path('panel_log_export_history/', views.panel_log_export_history, name='panel_log_export_history'),
    # TCP告警界面
    path('panel_tcp_warning/', views.panel_tcp_warning, name='panel_tcp_warning'),
    # UDP告警界面
    path('panel_udp_warning/', views.panel_udp_warning, name='panel_udp_warning'),
    # ICMP告警界面
    path('panel_icmp_warning/', views.panel_icmp_warning, name='panel_icmp_warning'),
    # 端口扫描告警界面
    path('panel_port_scan_warning/', views.panel_port_scan_warning, name='panel_port_scan_warning'),
    # 来源ip告警界面
    path('panel_srcip_warning/', views.panel_srcip_warning, name='panel_srcip_warning'),
    # 目的ip告警界面
    path('panel_dstip_warning/', views.panel_dstip_warning, name='panel_dstip_warning'),
    # 来源端口告警界面
    path('panel_srcport_warning/', views.panel_srcport_warning, name='panel_srcport_warning'),
    # 目的端口告警界面
    path('panel_dstport_warning/', views.panel_dstport_warning, name='panel_dstport_warning'),
    # 个人信息界面
    path('panel_profile/', views.panel_profile, name='panel_profile'),
    # 信息修改界面
    path('panel_profile_update/', views.panel_profile_update, name='panel_profile_update'),
    # 用户列表界面
    path('panel_user_list/', views.panel_user_list, name='panel_user_list'),
    # 创建用户界面
    path('panel_user_create/', views.panel_user_create, name='panel_user_create'),
    # 角色列表界面
    path('panel_role_list/', views.panel_role_list, name='panel_role_list'),
    # 创建角色界面
    path('panel_role_create/', views.panel_role_create, name='panel_role_create'),
    # 系统设置界面
    path('panel_setting/', views.panel_setting, name='panel_setting'),
    # 系统日志界面
    path('panel_system_log/', views.panel_system_log, name='panel_system_log'),
    # 关闭重启界面
    path('panel_shutdown_reboot/', views.panel_shutdown_reboot, name='panel_shutdown_reboot'),

    # 详细事件界面
    path('panel_event_detail/', views.panel_event_detail, name='panel_event_detail'),



    # 注销动作url
    path('action_logout/', actions.action_logout, name='action_logout'),
]
