from .models import Kakikomi
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Account

class KakikomiForm(forms.ModelForm):
    性別 = forms.fields.ChoiceField(
        choices=(
            ('1.0946','女'),
            ('0.5473','男')
        ),
            required=True,
            widget=forms.widgets.Select
    )
    運動 =  forms.fields.ChoiceField(
        choices=(
            ('1.2','週にほとんど運動しない'),
            ('1.375','週に１～２回程度運動する'),
            ('1.55','週に３～５回運動する'),
            ('1.725','週に６～７回程度運動する'),
            ('1.9','一日に2回程度運動する')
        )
    )
    アレルギー = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('えび',u'えび'),('かに',u'かに'),('卵',u'卵'),('落花生',u'落花生'),('そば',u'そば'),('乳',u'乳'),('小麦',u'小麦'),])
    class Meta:
        model = Kakikomi
        fields = ('名前', '身長' ,'体重','年齢')
        labels = {'名前':'名前', '身長':'身長' ,'体重':'体重','年齢':'年齢'}


class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    性別 = forms.fields.ChoiceField(
        choices=(
            ('1.0946','女'),
            ('0.5473','男')
        ),
            required=True,
            widget=forms.widgets.Select
    )
    運動 =  forms.fields.ChoiceField(
        choices=(
            ('1.2','週にほとんど運動しない'),
            ('1.375','週に１～２回程度運動する'),
            ('1.55','週に３～５回運動する'),
            ('1.725','週に６～７回程度運動する'),
            ('1.9','一日に2回程度運動する')
        )
    )
    アレルギー = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('えび',u'えび'),('かに',u'かに'),('卵',u'卵'),('落花生',u'落花生'),('そば',u'そば'),('乳',u'乳'),('小麦',u'小麦'),('0',u'無し'),])

    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('名前','身長','体重','年齢',)
        labels = {'名前':"名前",'身長':"身長",'体重':"体重",'年齢':"年齢",}