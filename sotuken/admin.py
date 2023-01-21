from django.contrib import admin

# Register your models here.
from .models import syokuzaibunrui
from .models import syokuzai
from .models import Account 
from .models import UserInfo

admin.site.register(Account)
admin.site.register(UserInfo)
admin.site.register(syokuzaibunrui)
admin.site.register(syokuzai)