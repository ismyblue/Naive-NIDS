from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse


class VerifyLogin(MiddlewareMixin):
    '''
    验证是否登录成功，判断是否有权限访问站点,未登录返回到login页面，若是登录成功且访问的是/nids/login,则返回到/nids/index
    '''

    def process_request(self, request):
        session = request.session
        # print(session.items())
        if 'login_status' not in session.keys() or not request.session['login_status']:
            if request.path != '/nids/panel_login/':
                return redirect(reverse('nids:panel_login'))
        elif request.path == '/nids/panel_login/' and request.session['login_status']:
            return redirect(reverse('nids:panel_main'))
