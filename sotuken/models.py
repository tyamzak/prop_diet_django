# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kakikomi(models.Model):
    id = models.BigAutoField(primary_key=True)
    名前 = models.CharField(max_length=100)
    身長 = models.IntegerField()
    体重 = models.IntegerField()
    年齢 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sotuken_kakikomi'


class syokuzaibunrui(models.Model):
    食材分類ID = models.IntegerField(db_column='食材分類ID', primary_key=True)  # Field name made lowercase.
    食材分類名 = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.食材分類名

    class Meta:
        managed = False
        db_table = '食材分類表'


class syokuzai(models.Model):
    食材id = models.IntegerField(db_column='食材ID', primary_key=True)  # Field name made lowercase.
    食材分類id = models.ForeignKey(syokuzaibunrui,models.DO_NOTHING, db_column='食材分類ID')  # Field name made lowercase.
    食材名 = models.CharField(max_length=45, blank=True, null=True)
    protein = models.FloatField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.
    carbohydrate = models.FloatField(db_column='Carbohydrate', blank=True, null=True)  # Field name made lowercase.
    kcal = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.食材名

    class Meta:
        managed = False
        db_table = '食材表'

class UserInfo(models.Model):
    id = models.AutoField(primary_key= True)
    登録名 = models.CharField(max_length=200)
    朝カロリー = models.FloatField(default=1)
    朝P = models.FloatField(default=1)
    朝F = models.FloatField(default=1)
    朝C = models.FloatField(default=1)
    昼カロリー = models.FloatField(default=1)
    昼P = models.FloatField(default=1)
    昼F = models.FloatField(default=1)
    昼C = models.FloatField(default=1)
    夜カロリー = models.FloatField(default=1)
    夜P = models.FloatField(default=1)
    夜F = models.FloatField(default=1)
    夜C = models.FloatField(default=1)
    アレルギー = models.TextField(max_length=200)
    user = models.ForeignKey(get_user_model(), verbose_name='ログインユーザー', default=1, on_delete=models.CASCADE)
   # user = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE)

    class Meta:
        db_table = 'sotuken_UserInfo'

    def __str__(self):
        return self.user.username

class Account(models.Model):
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 追加フィールド
    名前 = models.CharField(max_length=100)
    身長 = models.IntegerField(default=1)
    体重 = models.IntegerField(default=1)
    年齢 = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'sotuken_account'

    def __str__(self):
        return self.user.username




        



