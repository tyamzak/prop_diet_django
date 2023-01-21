# Generated by Django 4.1.5 on 2023-01-19 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kakikomi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('名前', models.CharField(max_length=100)),
                ('身長', models.IntegerField()),
                ('体重', models.IntegerField()),
                ('年齢', models.IntegerField()),
            ],
            options={
                'db_table': 'sotuken_kakikomi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='syokuzai',
            fields=[
                ('食材id', models.IntegerField(db_column='食材ID', primary_key=True, serialize=False)),
                ('食材名', models.CharField(blank=True, max_length=45, null=True)),
                ('protein', models.FloatField(blank=True, db_column='Protein', null=True)),
                ('fat', models.FloatField(blank=True, db_column='Fat', null=True)),
                ('carbohydrate', models.FloatField(blank=True, db_column='Carbohydrate', null=True)),
                ('kcal', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': '食材表',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='syokuzaibunrui',
            fields=[
                ('食材分類ID', models.IntegerField(db_column='食材分類ID', primary_key=True, serialize=False)),
                ('食材分類名', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': '食材分類表',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('登録名', models.CharField(max_length=200)),
                ('朝カロリー', models.FloatField(default=1)),
                ('朝P', models.FloatField(default=1)),
                ('朝F', models.FloatField(default=1)),
                ('朝C', models.FloatField(default=1)),
                ('昼カロリー', models.FloatField(default=1)),
                ('昼P', models.FloatField(default=1)),
                ('昼F', models.FloatField(default=1)),
                ('昼C', models.FloatField(default=1)),
                ('夜カロリー', models.FloatField(default=1)),
                ('夜P', models.FloatField(default=1)),
                ('夜F', models.FloatField(default=1)),
                ('夜C', models.FloatField(default=1)),
                ('アレルギー', models.TextField(max_length=200)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ログインユーザー')),
            ],
            options={
                'db_table': 'sotuken_UserInfo',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名前', models.CharField(max_length=100)),
                ('身長', models.IntegerField(default=1)),
                ('体重', models.IntegerField(default=1)),
                ('年齢', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sotuken_account',
            },
        ),
    ]
