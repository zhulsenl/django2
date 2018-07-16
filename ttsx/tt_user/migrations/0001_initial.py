# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', related_name='user_set', blank=True)),
            ],
            options={
                'db_table': 'df_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('receiver_name', models.CharField(verbose_name='收件人', max_length=20)),
                ('receiver_mobile', models.CharField(verbose_name='联系电话', max_length=11)),
                ('detail_addr', models.CharField(verbose_name='详细地址', max_length=256)),
                ('zip_code', models.CharField(verbose_name='邮政编码', max_length=6)),
            ],
            options={
                'db_table': 'df_address',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(null=True, to='tt_user.AreaInfo', blank=True)),
            ],
            options={
                'db_table': 'df_areainfo',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='city'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='district'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='provice'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
    ]
