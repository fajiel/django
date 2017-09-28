import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), u".."))

from database.psw_manage import PassWordManage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django import forms
# from database.models import User, AmazonUser, InternalMail, ExternalMail, OtherMail

MAIL_CFG = {
    1:"filter_mail.html",
    2:"filter_mail.html"
}
#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='账户',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

@csrf_exempt
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            pwm = PassWordManage()
            issucc = pwm.login(username, password)
            if issucc:
                # return render_to_response('filter_mail.html',{'username': username})
                return HttpResponseRedirect('/filter_mail/?usr={}'.format(username))
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf})

def filter_mail(request):
    from database.manage import Session
    from database.models import AmazonUser
    username = request.GET.get("usr")
    session = Session()
    query = session.query(AmazonUser.name, AmazonUser.level)
    query_obj = query.filter_by(name=username).first()
    level = query_obj.level
    template = MAIL_CFG.get(level)
    return render_to_response(template)
