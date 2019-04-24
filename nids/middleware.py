from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse


class VerifyLogin(MiddlewareMixin):
    '''
    验证是否登录成功，判断是否有权限访问站点,未登录返回到login页面，若是登录成功且访问的是/nids/login,则返回到/nids/index
    '''

    def process_request(self, request):
        session = request.session
        if 'login_status' not in session.keys() or not request.session['login_status']:
            if request.path != '/nids/panel_login/':
                return redirect(reverse('nids:panel_login'))
        elif request.path == '/nids/panel_login/' and request.session['login_status']:
            return redirect(reverse('nids:panel_main'))


class FillUserInfo(MiddlewareMixin):
    """
    对每一个utl，都填用户名到模板中{{ usr_login }}
    """

    def process_template_response(self, request, response):
        if request.session['login_status'] and 'usr_name' in request.session.keys():
            usr_name = request.session['usr_name']
            response.context_data['usr_name'] = usr_name
        return response


