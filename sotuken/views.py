import imp
from multiprocessing import context
from operator import imod
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from sotuken.forms import KakikomiForm
from . import forms
from . forms import KakikomiForm
from . models import Kakikomi
from . models import UserInfo
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm #ユーザー
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def keisan(request):
    form = AddAccountForm(request.POST)
    paramas = {
        '基礎代謝':'基礎代謝',
        'f':AddAccountForm(),
        'TDEE':'TDEE',
        '総消費カロリー':'総消費カロリー',
        '目標カロリー':'目標カロリー',
        'BMI':'BMI',
        '減量目標':'減量目標',
        'アレルギー':request.POST.getlist("アレルギー"),
    }
    if request.method == 'POST':
        if (float(request.POST['性別']) == 0.5473):
            hp1 = 66.47
            hp2 = 13.75
            hp3 = 5
            hp4 = 6.76
        else:
            hp1 = 655.1
            hp2 = 9.56
            hp3 = 1.85
            hp4 = 4.68
        paramas['基礎代謝']=hp1 + hp2 *float(request.POST['体重']) + hp3 *float(request.POST['身長']) - hp4 * float(request.POST['年齢'])
        paramas['TDEE']=float(request.POST['運動'])
        paramas['f'] = AddAccountForm(request.POST)
        paramas['総消費カロリー']=float(paramas['TDEE']*paramas['基礎代謝'])
        paramas['BMI']=float(request.POST['体重'])/float(int(request.POST['身長'])*int(request.POST['身長']) / 10000)
        if (float(paramas['BMI']) >= 35):
            mp = 0.05
        else:
            mp = 0.03
        paramas['減量目標']= mp*float(request.POST['体重'])
        paramas['目標カロリー']=paramas['総消費カロリー'] - (paramas['減量目標']*7000/90)
        paramas['朝']=paramas['目標カロリー']*0.3
        paramas['昼']=paramas['目標カロリー']*0.3
        paramas['晩']=paramas['目標カロリー']*0.4
        paramas['朝P']=paramas['朝']*0.2/4
        paramas['朝F']=paramas['朝']*0.2/9
        paramas['朝C']=paramas['朝']*0.6/4
        paramas['昼P']=paramas['昼']*0.2/4
        paramas['昼F']=paramas['昼']*0.2/9
        paramas['昼C']=paramas['昼']*0.6/4
        paramas['晩P']=paramas['晩']*0.2/4
        paramas['晩F']=paramas['晩']*0.2/9
        paramas['晩C']=paramas['晩']*0.6/4

    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
       UserInfo.objects.create( 登録名 = request.POST['名前'], 目標カロリー = paramas['目標カロリー'], 朝P = paramas['朝P'], 朝F = paramas['朝F'], 朝C = paramas['朝C'], 昼P = paramas['昼P'], 昼F = paramas['昼F'], 昼C = paramas['昼C'], 夜P = paramas['夜P'], 夜F = paramas['夜F'], 夜C = paramas['夜C'], アレルギー = paramas['アレルギー'], )

    return render(request, 'sotuken/KakikomiForm.html',paramas)

class SampleChoiceView(View):
    def get(self,request):
        form = forms.SampleChoiceForm()
        context = {
            'form': form
        }
        return render(request, 'sotuken/KakikomiForm.html',context)
        sample_choice_view = SampleChoiceView.as_view()


def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'sotuken/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "sotuken/home.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"sotuken/register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)
    
        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
             paramas = {
                '基礎代謝':'基礎代謝',
                'f':AddAccountForm(),
                'TDEE':'TDEE',
                '総消費カロリー':'総消費カロリー',
                '目標カロリー':'目標カロリー',
                'BMI':'BMI',
                '減量目標':'減量目標',
                'アレルギー':request.POST.getlist("アレルギー"),
             }
             if (float(request.POST['性別']) == 0.5473):
                 hp1 = 66.47
                 hp2 = 13.75
                 hp3 = 5
                 hp4 = 6.76
             else:
                 hp1 = 655.1
                 hp2 = 9.56
                 hp3 = 1.85
                 hp4 = 4.68
             paramas['基礎代謝']=hp1 + hp2 *float(request.POST['体重']) + hp3 *float(request.POST['身長']) - hp4 * float(request.POST['年齢'])
             paramas['TDEE']=float(request.POST['運動'])
             paramas['f'] = AddAccountForm(request.POST)
             paramas['総消費カロリー']=float(paramas['TDEE']*paramas['基礎代謝'])
             paramas['BMI']=float(request.POST['体重'])/float(int(request.POST['身長'])*int(request.POST['身長']) / 10000)
             if (float(paramas['BMI']) >= 35):
                 mp = 0.05
             else:
                 mp = 0.03
             paramas['減量目標']= mp*float(request.POST['体重'])
             paramas['目標カロリー']=paramas['総消費カロリー'] - (paramas['減量目標']*7000/90)
             paramas['朝']=paramas['目標カロリー']*0.3
             paramas['昼']=paramas['目標カロリー']*0.3
             paramas['晩']=paramas['目標カロリー']*0.4
             paramas['朝P']=paramas['朝']*0.2/4
             paramas['朝F']=paramas['朝']*0.2/9
             paramas['朝C']=paramas['朝']*0.6/4
             paramas['昼P']=paramas['昼']*0.2/4
             paramas['昼F']=paramas['昼']*0.2/9
             paramas['昼C']=paramas['昼']*0.6/4
             paramas['晩P']=paramas['晩']*0.2/4
             paramas['晩F']=paramas['晩']*0.2/9
             paramas['晩C']=paramas['晩']*0.6/4
             userinfo = UserInfo(登録名 = request.POST['名前'], 朝カロリー = (paramas['目標カロリー']*3/10), 昼カロリー = (paramas['目標カロリー']*3/10), 夜カロリー = (paramas['目標カロリー']*4/10),朝P = paramas['朝P'], 朝F = paramas['朝F'], 朝C = paramas['朝C'], 昼P = paramas['昼P'], 昼F = paramas['昼F'], 昼C = paramas['昼C'], 夜P = paramas['晩P'], 夜F = paramas['晩F'], 夜C = paramas['晩C'], アレルギー = paramas['アレルギー'] )

            # アカウント情報をDB保存
             account = self.params["account_form"].save()
            # パスワードをハッシュ化
             account.set_password(account.password)
             # ハッシュ化パスワード更新
             account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
             add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
             userinfo.user = account
             add_account.user = account
            

            # モデル保存
             add_account.save()
             
             userinfo.save()

            # アカウント作成情報更新
             self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"sotuken/register.html",context=self.params)

    def keisan(self,request):
        form = AddAccountForm(request.POST)
        paramas = {
        '基礎代謝':'基礎代謝',
        'f':AddAccountForm(),
        'TDEE':'TDEE',
        '総消費カロリー':'総消費カロリー',
        '目標カロリー':'目標カロリー',
        'BMI':'BMI',
        '減量目標':'減量目標',
        'アレルギー':request.POST.getlist("アレルギー"),
        }
        if request.method == 'POST':
            if (float(request.POST['性別']) == 0.5473):
                hp1 = 66.47
                hp2 = 13.75
                hp3 = 5
                hp4 = 6.76
            else:
                hp1 = 655.1
                hp2 = 9.56
                hp3 = 1.85
                hp4 = 4.68
            paramas['基礎代謝']=hp1 + hp2 *float(request.POST['体重']) + hp3 *float(request.POST['身長']) - hp4 * float(request.POST['年齢'])
            paramas['TDEE']=float(request.POST['運動'])
            paramas['f'] = AddAccountForm(request.POST)
            paramas['総消費カロリー']=float(paramas['TDEE']*paramas['基礎代謝'])
            paramas['BMI']=float(request.POST['体重'])/float(int(request.POST['身長'])*int(request.POST['身長']) / 10000)
            if (float(paramas['BMI']) >= 35):
                 mp = 0.05
            else:
                 mp = 0.03
            paramas['減量目標']= mp*float(request.POST['体重'])
            paramas['目標カロリー']=paramas['総消費カロリー'] - (paramas['減量目標']*7000/90)
            paramas['朝']=paramas['目標カロリー']*0.3
            paramas['昼']=paramas['目標カロリー']*0.3
            paramas['晩']=paramas['目標カロリー']*0.4
            paramas['朝P']=paramas['朝']*0.2/4
            paramas['朝F']=paramas['朝']*0.2/9
            paramas['朝C']=paramas['朝']*0.6/4
            paramas['昼P']=paramas['昼']*0.2/4
            paramas['昼F']=paramas['昼']*0.2/9
            paramas['昼C']=paramas['昼']*0.6/4
            paramas['晩P']=paramas['晩']*0.2/4
            paramas['晩F']=paramas['晩']*0.2/9
            paramas['晩C']=paramas['晩']*0.6/4

            UserInfo.objects.create( 登録名 = request.POST['名前'], 目標カロリー = paramas['目標カロリー'], 朝P = paramas['朝P'], 朝F = paramas['朝F'], 朝C = paramas['朝C'], 昼P = paramas['昼P'], 昼F = paramas['昼F'], 昼C = paramas['昼C'], 夜P = paramas['夜P'], 夜F = paramas['夜F'], 夜C = paramas['夜C'], アレルギー = paramas['アレルギー'], ユーザーid = self.request.user,)

            return render(request, 'sotuken/home',paramas)
