from django.urls import path
from nids import views, actions


app_name = 'nids'
urlpatterns = [
    # # 首页界面url
    path('', views.panel_login, name='panel_index'),
    # 登录界面url，包括登录动作
    path('panel_login/', views.panel_login, name='panel_login'),
    # 控制台主界面
    path('panel_main/', views.panel_main, name='panel_main'),
    # 欢迎界面，告警信息统计界面
    path('panel_welcome/', views.panel_welcome, name='panel_welcome'),
    # 最新告警界面
    path('panel_latest_warning/<int:page_num>/', views.panel_latest_warning, name='panel_latest_warning'),
    # 日志查询界面
    path('panel_log_query/', views.panel_log_query, name='panel_log_query'),
    # 日志导出记录界面
    path('panel_log_export_history/', views.panel_log_export_history, name='panel_log_export_history'),
    # TCP告警界面
    path('panel_tcp_warning/<int:page_num>/', views.panel_tcp_warning, name='panel_tcp_warning'),
    # UDP告警界面
    path('panel_udp_warning/<int:page_num>/', views.panel_udp_warning, name='panel_udp_warning'),
    # ICMP告警界面
    path('panel_icmp_warning/<int:page_num>/', views.panel_icmp_warning, name='panel_icmp_warning'),
    # 端口扫描告警界面
    path('panel_port_scan_warning/<int:page_num>/', views.panel_port_scan_warning, name='panel_port_scan_warning'),
    # 来源ip告警界面
    path('panel_srcip_warning/<int:page_num>/', views.panel_srcip_warning, name='panel_srcip_warning'),
    # 目的ip告警界面
    path('panel_dstip_warning/<int:page_num>/', views.panel_dstip_warning, name='panel_dstip_warning'),
    # 来源端口告警界面
    path('panel_srcport_warning/', views.panel_srcport_warning, name='panel_srcport_warning'),
    # 目的端口告警界面
    path('panel_dstport_warning/', views.panel_dstport_warning, name='panel_dstport_warning'),
    # 个人信息界面
    path('panel_profile/', views.panel_profile, name='panel_profile'),
    # 信息修改界面 信息修改动作
    path('panel_profile_update/', views.panel_profile_update, name='panel_profile_update'),
    # 用户列表界面
    path('panel_user_list/<int:page_num>/', views.panel_user_list, name='panel_user_list'),
    # 用户更新界面
    path('panel_user_update/<int:usr_id>/', views.panel_user_update, name='panel_user_update'),
    # 创建用户界面
    path('panel_user_create/', views.panel_user_create, name='panel_user_create'),
    # 角色列表界面
    path('panel_role_list/<int:page_num>/', views.panel_role_list, name='panel_role_list'),
    # 角色更新界面
    path('panel_role_update/<int:role_id>/', views.panel_role_update, name='panel_role_update'),
    # 创建角色界面
    path('panel_role_create/', views.panel_role_create, name='panel_role_create'),
    # 系统设置界面
    path('panel_setting/', views.panel_setting, name='panel_setting'),
    # 系统日志界面
    path('panel_system_log/', views.panel_system_log, name='panel_system_log'),
    # 关闭重启界面
    path('panel_shutdown_reboot/', views.panel_shutdown_reboot, name='panel_shutdown_reboot'),

    # 详细事件界面
    path('panel_event_detail/<int:eid>/', views.panel_event_detail, name='panel_event_detail'),
    # 源ip所有事件列表
    path('panel_ip_src_list/<str:ip_src>/', views.panel_ip_src_list, name='panel_ip_src_list'),
    # 目的ip所有事件列表
    path('panel_ip_dst_list/<str:ip_src>/', views.panel_ip_dst_list, name='panel_ip_dst_list'),



    # 注销动作url
    path('action_logout/', actions.action_logout, name='action_logout'),
    #删除用户动作
    path('action_user_delete/<int:usr_id>/', actions.action_user_delete, name='action_user_delete'),
    # 删除角色动作
    path('action_role_delete/<int:role_id>/', actions.action_role_delete, name='action_role_delete'),
    # 删除告警动作
    path('action_warning_delete/<int:warning_id>/', actions.action_warning_delete, name='action_warning_delete'),


]
